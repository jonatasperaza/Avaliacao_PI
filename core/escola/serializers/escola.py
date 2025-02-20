from rest_framework import serializers
from core.escola.modelosteste import Escola

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id', 'nome', 'endereco', 'telefone']