import operator
import re
from functools import reduce

from django.db import models
from django.db.models import F
from rest_framework.compat import distinct
from rest_framework.filters import OrderingFilter as BaseOrderingFilter
from rest_framework.filters import SearchFilter as BaseSearchFilter

# マックス100%でannotateする(そうしなければ誤差が顕著にでる)
# 小数にしないとFがint型で計算してしまう
PERCENT = 100.0

SORT_GRADE_LIST = [
    'f', '-f', 'failure', '-failure', 'a_band', '-a_band'
]

REPLACE_ROMAN_FIGURE = [
    ('1', 'Ⅰ'), ('１', 'Ⅰ'), ('2', 'Ⅱ'), ('２', 'Ⅱ'),
    ('3', 'Ⅲ'), ('３', 'Ⅲ'), ('4', 'Ⅳ'), ('４', 'Ⅳ'),
    ('5', 'Ⅴ'), ('５', 'Ⅴ'), ('6', 'Ⅵ'), ('６', 'Ⅵ'),
    ('7', 'Ⅶ'), ('７', 'Ⅶ'), ('8', 'Ⅷ'), ('８', 'Ⅷ'),
    ('9', 'Ⅸ'), ('９', 'Ⅸ')
]


class OrderingFilter(BaseOrderingFilter):

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        new_ordering = []
        annotate_kwargs = {}
        for i in range(len(ordering)):

            if ordering[i] not in SORT_GRADE_LIST:
                new_ordering.append(ordering[i])
                continue

            # f
            if ordering[i] in ['f', '-f']:
                annotate_kwargs.setdefault(
                    "f_percent",
                    PERCENT * F('f') / F('numOfStudents')
                )
                new_ordering.append(ordering[i] + '_percent')
            elif ordering[i] in ['failure', '-failure']:
                annotate_kwargs.setdefault(
                    "failure_percent",
                    PERCENT * (F('d') + F('dm') + F('f')) / F('numOfStudents')
                )
                new_ordering.append(ordering[i] + '_percent')
                gpa_ordering = 'gpa' if ordering[i][0] == '-' else '-gpa'
                new_ordering.append(gpa_ordering)

            elif ordering[i] in ['a_band', '-a_band']:
                annotate_kwargs.setdefault(
                    "a_band_percent",
                    PERCENT * (F('ap') + F('a') + F('am')) / F('numOfStudents')
                )
                new_ordering.append(ordering[i] + '_percent')
                gpa_ordering = '-gpa' if ordering[i][0] == '-' else 'gpa'
                new_ordering.append(gpa_ordering)

        queryset = queryset.annotate(**annotate_kwargs)

        if new_ordering:
            return queryset.order_by(*new_ordering)

        return queryset


class SearchFilter(BaseSearchFilter):

    def get_filter_query(self, request, queryset, view, search_terms):
        search_fields = self.get_search_fields(view, request)

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]

        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))

        return reduce(operator.and_, conditions)

    def replace_terms(self, terms, REPLACE_WORDS):
        replaced_terms = []
        for term in terms:
            term = reduce(lambda accum, args: accum.replace(*args), REPLACE_WORDS, term)
            replaced_terms.append(term)

        return replaced_terms

    def replace_japanese_year(self, params):

        def year_repl(matchobj):
            return matchobj[0][:4]

        params = re.sub(r'\d\d\d\d年度?', year_repl, params)
        return params

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        params = self.replace_japanese_year(params)
        return params.split()

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        search_terms_list = [search_terms]
        search_terms_list.append(self.replace_terms(search_terms, REPLACE_ROMAN_FIGURE))

        conditions = []
        base = queryset
        for s_terms in search_terms_list:
            model_Q = self.get_filter_query(request, queryset, view, s_terms)
            conditions.append(model_Q)

        queryset = queryset.filter(reduce(operator.or_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            # Filtering against a many-to-many field requires us to
            # call queryset.distinct() in order to avoid duplicate items
            # in the resulting queryset.
            # We try to avoid this if possible, for performance reasons.
            queryset = distinct(queryset, base)
        return queryset
