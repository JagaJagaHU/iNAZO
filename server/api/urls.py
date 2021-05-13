from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('gradeinfo/', views.GradeInfoList.as_view()),
    path('gradeinfo/<int:pk>/', views.GradeInfoDetail.as_view()),
    path('bookmark/', views.BookMarkList.as_view()),
    path('bookmark/<int:pk>/', views.BookMarkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)