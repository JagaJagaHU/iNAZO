from io import StringIO

from django.test import TestCase
from django.core.management import call_command

from api.models import GradeInfo


class CommandTest(TestCase):

    def test_loadalldata(self):
        out = StringIO()  # stdoutに出力しない
        call_command('loadalldata', stdout=out)
        isSaved = GradeInfo.objects.exists()
        self.assertTrue(isSaved)
