from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAdminUser

from .serializers import GradeInfoSerializer
from .models import GradeInfo
from .permissions import ReadOnly

class GradeInfoList(generics.ListCreateAPIView):

    queryset = GradeInfo.objects.all()
    serializer_class = GradeInfoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAdminUser|ReadOnly]
    search_fields = [
        'subject', 'lecture', 'group', 'teacher', 'year', 'semester',
        'faculty',
    ]
    ordering_fields = '__all__'
    ordering = ['-year', 'semester']

class GradeInfoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = GradeInfo.objects.all()
    serializer_class = GradeInfoSerializer
    permission_classes = [IsAdminUser|ReadOnly]