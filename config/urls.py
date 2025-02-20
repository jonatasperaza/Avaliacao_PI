# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'alunos': reverse('aluno-list', request=request, format=format),
        'professores': reverse('professor-list', request=request, format=format),
        'escolas': reverse('escola-list', request=request, format=format),
        'turmas': reverse('turma-list', request=request, format=format),
        'cordenacao': reverse('cordenacao-root', request=request, format=format),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('core.escola.urls')),  # Inclui as rotas principais
    path('api/cordenacao/', include('core.escola.cordenacao.urls')),  # Inclui as rotas de cordenacao
]
