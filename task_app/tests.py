from django.test import TestCase


class HomeTestCase(TestCase):
    def test_home_path(self):
        """Возвращается ли страница '/' и равен ли  HTTP код возврата 200"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
