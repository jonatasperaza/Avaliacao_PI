# core/escola/cordenacao/urls.py
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter
from .views import CordenacaoTesteViewSet  # Certifique-se de que o nome da view está correto

router = DefaultRouter()
router.register(r'teste', CordenacaoTesteViewSet, basename='cordenacao-teste')

@api_view(['GET'])
def cordenacao_root(request, format=None):
    return Response({
        'teste': reverse('cordenacao-teste-list', request=request, format=format),
        # Adicione outras rotas aqui conforme necessário
    })

urlpatterns = [
    path('', cordenacao_root, name='cordenacao-root'),
    path('', include(router.urls)),
]
