from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.escola_data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '1234567890'
        }

    def test_create_escola(self):
        response = self.client.post(
            '/api/escolas/',
            self.escola_data,
            format='json'
        )
        print("Response:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_escolas(self):
        response = self.client.get('/api/escolas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
