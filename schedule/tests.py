from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TimeTest(APITestCase):

    def setUp(self):
        self.time_url = reverse('drtimes')

    def test_time_get(self):
        self.response = self.client.get(self.time_url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
