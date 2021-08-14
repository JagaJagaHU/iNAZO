from rest_framework.test import APITestCase
from rest_framework import status


class FilterTest(APITestCase):

    fixtures = ['test_data.json']

    def test_search_roman_figure(self):
        ROMAN_FIGURES = [
            'Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ',
            'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ',
            'Ⅸ',
        ]
        # アラビア数字で検索
        for i in range(1, 10):
            response = self.client.get(f'/api/gradeinfo/?search=test{i}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            res = response.json()['results']
            self.assertEqual(len(res), 1)
            self.assertEqual(res[0]['subject'], f'test{ROMAN_FIGURES[i-1]}')

        # ローマ数字で検索
        for i in range(1, 10):
            response = self.client.get(f'/api/gradeinfo/?search=test{ROMAN_FIGURES[i-1]}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            res = response.json()['results']
            self.assertEqual(len(res), 1)
            self.assertEqual(res[0]['subject'], f'test{ROMAN_FIGURES[i-1]}')
