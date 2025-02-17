"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from core.escola.views.user import UserViewSet
from core.escola.views.aluno import AlunoViewSet
from core.escola.views.professor import ProfessorViewSet
from core.escola.views.escola import EscolaViewSet
from core.escola.views.turma import TurmaViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'escolas', EscolaViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', lambda request: redirect('api/')),
]
