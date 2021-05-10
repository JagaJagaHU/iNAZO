import json

from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from .models import GradeInfo
from .views import GradeInfoList, GradeInfoDetail
from .serializers import GradeInfoSerializer
from .paginations import get_num_page

class GradeInfoAPITest(TestCase):

    fixtures = ['test_data.json']

    def setUp(self):
        self.dataSize = len(GradeInfo.objects.all())
        self.factory = APIRequestFactory()
        self.data = {
            "subject": "プログラミング入門",
            "lecture": "テストの必要性",
            "group": "1-53組",
            "teacher": "手巣戸　大事",
            "year": "2200",
            "semester": "2学期",
            "faculty": "総合教育部",
            "numOfStudents": 1000,
            "ap": 0,
            "a": 0,
            "am": 0,
            "bp": 0,
            "b": 0,
            "bm": 0,
            "cp": 0,
            "c": 0,
            "d": 0,
            "dm": 0,
            "f": 1000,
            "gpa": 0,
        }
        self.user = User.objects.create_user(
            username='testuser', email='jaco@test.jp', password='top_secret'
        )
        self.admin = User.objects.create_superuser(
            username='supertestuser', email='jacob@test.com', password='top_secret'
        )
        self.listView = GradeInfoList.as_view()
        self.detailView = GradeInfoDetail.as_view()
    
    def test_get(self):
        request = self.factory.get('/api/gradeinfo/')
        response = self.listView(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.dataSize)

    def test_post_by_anonymousUser(self):
        request = self.factory.post('/api/gradeinfo/', self.data)
        response = self.listView(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_post_by_user(self):
        request = self.factory.post('/api/gradeinfo/', self.data)
        force_authenticate(request, user=self.user)
        response = self.listView(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_post_by_admin(self):
        request = self.factory.post('/api/gradeinfo/', self.data)
        force_authenticate(request, user=self.admin)
        response = self.listView(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(GradeInfo.objects.all()), self.dataSize+1)
    
    
    def test_retrieve(self):
        request = self.factory.get('/api/gradeinfo/1/', self.data)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
    
    
    def test_put_by_anonymousUser(self):
        request = self.factory.put('/api/gradeinfo/1/', self.data)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_put_by_user(self):
        request = self.factory.put('/api/gradeinfo/1/', self.data)
        force_authenticate(request, user=self.user)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_put_by_admin(self):
        request = self.factory.put('/api/gradeinfo/1/', self.data)
        force_authenticate(request, user=self.admin)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        gi = GradeInfo.objects.get(pk=1)
        self.assertEqual(gi.subject, "プログラミング入門")
    

    def test_delete_by_anonymousUser(self):
        request = self.factory.delete('/api/gradeinfo/1/')
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_delete_by_user(self):
        request = self.factory.delete('/api/gradeinfo/1/')
        force_authenticate(request, user=self.user)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_delete_by_admin(self):
        request = self.factory.delete('/api/gradeinfo/1/')
        force_authenticate(request, user=self.admin)
        response = self.detailView(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        qs = GradeInfo.objects.filter(pk=1)
        self.assertFalse(qs.exists())

    def test_calc_num_page(self):
        inputs = [100, 101, 99]
        if settings.REST_FRAMEWORK['PAGE_SIZE'] != 10:
            raise Exception("ページサイズが変更されました。テストコードを見直す必要があります。")
        page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
        ans = [10, 11, 10]
        res = [get_num_page(inp, page_size) for inp in inputs]
        self.assertEqual(res, ans)
