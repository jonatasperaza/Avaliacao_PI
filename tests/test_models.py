from django.test import TestCase
from django.contrib.auth import get_user_model
from core.escola.models import Escola, Turma, Professor, Aluno
from datetime import date

class ModelTestCase(TestCase):
    def setUp(self):
        # Criar usuário básico primeiro
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com',
            first_name='Test',
            last_name='User'
        )
        
        # Criar escola
        self.escola = Escola.objects.create(
            nome='Escola Teste',
            endereco='Rua Teste, 123',
            telefone='1234567890'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_escola_creation(self):
        self.assertEqual(self.escola.nome, 'Escola Teste')
