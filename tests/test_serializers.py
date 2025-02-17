from django.test import TestCase
from core.escola.serializers import EscolaSerializer, ProfessorSerializer
from core.escola.models import Escola

class SerializerTestCase(TestCase):
    def setUp(self):
        self.escola_data = {
            'nome': 'Escola Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '1234567890'
        }

    def test_escola_serializer(self):
        serializer = EscolaSerializer(data=self.escola_data)
        is_valid = serializer.is_valid()
        if not is_valid:
            print("Erros:", serializer.errors)
        self.assertTrue(is_valid)
