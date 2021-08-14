import os
import json

from django.core.management.base import BaseCommand

from api.models import GradeInfo


def save_recode_if_not_exist(data):
    for gradeData in data:
        record = gradeData['fields']
        if not GradeInfo.objects.filter(**record).exists():
            GradeInfo.objects.create(**record)


class Command(BaseCommand):

    help = 'load all json data without overwriting.'

    def add_arguments(self, parser):
        parser.add_argument('--test', action='store_true')

    def handle(self, *args, **options):

        dataDir = "scraping/testdata/" if options.get("test") else "scraping/data/"

        for curDir, dirs, files in os.walk(dataDir):
            for filename in files:
                filePath = os.path.join(curDir, filename)
                self.stdout.write(filePath)

                with open(filePath, 'r') as f:
                    data = json.load(f)
                    save_recode_if_not_exist(data)
