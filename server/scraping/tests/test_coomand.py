from io import StringIO

from django.core.management import call_command
from django.test import Client, TestCase

from api.models import GradeInfo


class CommandTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_loadalldata(self):
        expected = 6
        out = StringIO()  # stdoutに出力しない
        call_command('loadalldata', stdout=out, test=True)
        actual = GradeInfo.objects.count()
        self.assertEqual(actual, expected)

    def test_not_clean_bookmark_by_loadalldata(self):
        # 一度データ登録
        out = StringIO()  # stdoutに出力しない
        call_command('loadalldata', stdout=out, test=True)
        first = GradeInfo.objects.first()
        bookmarkID = str(first.id)
        data = {
            'bookMarkID': bookmarkID,
        }
        response = self.client.post("/api/bookmark/", data)
        response = self.client.get("/api/bookmark/")
        actual = len(response.json())
        expected = 1
        self.assertEqual(actual, expected)
        # もう一度呼ぶ
        call_command('loadalldata', stdout=out, test=True)
        response = self.client.get("/api/bookmark/")
        actual = len(response.json())
        expected = 1
        self.assertEqual(actual, expected)
