from rest_framework import serializers
from core.escola.cordenacao.models import teste

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = teste
        fields = '__all__'

