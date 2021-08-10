import os

from django.core.management.base import BaseCommand
from django.core.management import call_command

from api.models import GradeInfo


class Command(BaseCommand):

    help = 'delete all gradeinfo table data and load all json data.'

    def add_arguments(self, parser):
        parser.add_argument('--test', action='store_true')

    def handle(self, *args, **options):

        text = 'このコマンドはgradeinfoテーブルのデータを全て消去します。よろしいですか？[y/n] : '
        if GradeInfo.objects.exists() and input(text) != 'y':
            return

        GradeInfo.objects.all().delete()

        dataDir = "scraping/testdata/" if options.get("test") else "scraping/data/"

        for curDir, dirs, files in os.walk(dataDir):
            for filename in files:
                filePath = os.path.join(curDir, filename)
                self.stdout.write(filePath)
                command_args = ['loaddata', filePath]
                call_command(*command_args, stdout=self.stdout)
