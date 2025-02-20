# core/escola/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.aluno import AlunoViewSet
from .views.professor import ProfessorViewSet
from .views.escola import EscolaViewSet
from .views.turma import TurmaViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'escolas', EscolaViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
