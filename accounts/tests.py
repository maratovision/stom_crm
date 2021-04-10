from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class DoctorsTest(APITestCase):

    def setUp(self):
        self.doctor_url = reverse('staff')

    def test_doctors_get(self):
        self.response = self.client.get(self.doctor_url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
