from io import StringIO

from django.test import TestCase
from django.core.management import call_command

from api.models import GradeInfo


class CommandTest(TestCase):

    def test_loadalldata(self):
        expected = 6
        out = StringIO()  # stdoutに出力しない
        call_command('loadalldata', stdout=out, test=True)
        actual = GradeInfo.objects.count()
        self.assertEqual(actual, expected)
