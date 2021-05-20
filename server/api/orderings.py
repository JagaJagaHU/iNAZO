from django.db.models import F
from rest_framework.filters import OrderingFilter as BaseOrderingFilter

# マックス100%でannotateする(そうしなければ誤差が顕著にでる)
PERCENT = 100

SORT_GRADE_LIST = [
    'ap', '-ap', 'a', '-a', 'am', '-am',
    'bp', '-bp', 'b', '-b', 'bm', '-bm',
    'cp', '-cp', 'c', '-c', 'd', '-d',
    'dm', '-dm', 'f', '-f',
]


class OrderingFilter(BaseOrderingFilter):

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        new_ordering = []
        for i in range(len(ordering)):

            if ordering[i] not in SORT_GRADE_LIST:
                new_ordering.append(ordering[i])
                continue

            # ap
            if ordering[i] in ['ap', '-ap']:
                queryset = queryset.annotate(
                    ap_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # a
            elif ordering[i] in ['a', '-a']:
                queryset = queryset.annotate(
                    a_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # am
            elif ordering[i] in ['am', '-am']:
                queryset = queryset.annotate(
                    am_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # bp
            elif ordering[i] in ['bp', '-bp']:
                queryset = queryset.annotate(
                    bp_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # b
            elif ordering[i] in ['b', '-b']:
                queryset = queryset.annotate(
                    b_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # bm
            elif ordering[i] in ['bm', '-bm']:
                queryset = queryset.annotate(
                    bm_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # cp
            elif ordering[i] in ['cp', '-cp']:
                queryset = queryset.annotate(
                    cp_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # c
            elif ordering[i] in ['c', '-c']:
                queryset = queryset.annotate(
                    c_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # d
            elif ordering[i] in ['d', '-d']:
                queryset = queryset.annotate(
                    d_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # dm
            elif ordering[i] in ['dm', '-dm']:
                queryset = queryset.annotate(
                    dm_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )
            # f
            elif ordering[i] in ['f', '-f']:
                queryset = queryset.annotate(
                    f_percent=PERCENT * F(self.remove_prefix_underbar(ordering[i])) / F('numOfStudents')
                )

            new_ordering.append(ordering[i] + '_percent')
            new_ordering.append(ordering[i])

        if new_ordering:
            return queryset.order_by(*new_ordering)

        return queryset

    def remove_prefix_underbar(self, s):
        return s.strip('-')
