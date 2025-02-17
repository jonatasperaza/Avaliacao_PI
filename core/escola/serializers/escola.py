from rest_framework import serializers
from core.escola.models import Escola

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id', 'nome', 'endereco', 'telefone']