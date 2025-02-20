from rest_framework import serializers
from core.escola.modelosteste import Turma


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        read_only_fields = ['id']