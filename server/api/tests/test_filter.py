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
        FULL_WIDTH_CHARACTER = [chr(i) for i in range(ord('１'), ord('９') + 1)]
        # アラビア数字で検索
        for i in range(1, 10):
            response = self.client.get(f'/api/gradeinfo/?search=test{i}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            res = response.json()['results']
            self.assertEqual(len(res), 1)
            self.assertEqual(res[0]['subject'], f'test{ROMAN_FIGURES[i-1]}')

        # 全角数字で検索
        for i, full in enumerate(FULL_WIDTH_CHARACTER):
            response = self.client.get(f'/api/gradeinfo/?search=test{full}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            res = response.json()['results']
            self.assertEqual(len(res), 1)
            self.assertEqual(res[0]['subject'], f'test{ROMAN_FIGURES[i]}')

        # ローマ数字で検索
        for i in range(1, 10):
            response = self.client.get(f'/api/gradeinfo/?search=test{ROMAN_FIGURES[i-1]}')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            res = response.json()['results']
            self.assertEqual(len(res), 1)
            self.assertEqual(res[0]['subject'], f'test{ROMAN_FIGURES[i-1]}')

    def test_ordering_filter(self):
        # f (昇順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=f')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [13, 15, 14])

        # f (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-f')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [14, 15, 13])

        # failure (昇順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=failure')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [13, 15, 14])

        # failure (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-failure')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [14, 15, 13])

        # a_band (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=a_band')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [13, 14, 15])

        # a_band (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-a_band')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [15, 14, 13])

        # gpa (昇順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=gpa')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [13, 14, 15])

        # gpa (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-gpa')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [15, 14, 13])

        # year (昇順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=year')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [15, 13, 14])

        # year (降順)
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-year')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [14, 13, 15])

        # default
        response = self.client.get('/api/gradeinfo/?search=ordering&ordering=-year')
        actual = self.get_pk_from_list(response.json()['results'])
        self.assertEqual(actual, [14, 13, 15])

    @staticmethod
    def get_pk_from_list(arr):
        return list(map(lambda x: x['id'], arr))
