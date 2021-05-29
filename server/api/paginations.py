import math

from rest_framework import pagination
from rest_framework.response import Response


def get_num_page(count, page_size):
    return math.ceil(count / page_size)


class SizePagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'size': get_num_page(self.page.paginator.count, self.page_size),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
