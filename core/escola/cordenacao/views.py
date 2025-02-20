from django.shortcuts import render
from rest_framework import viewsets

from core.escola.cordenacao.models import teste
from .serializer import TesteSerializer

class CordenacaoTesteViewSet(viewsets.ModelViewSet):
    queryset = teste.objects.all()
    serializer_class = TesteSerializer



# Create your views here.
