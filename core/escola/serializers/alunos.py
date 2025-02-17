from rest_framework import serializers
from core.escola.models import Aluno
from core.escola.serializers.user import UserSerializer

class AlunoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Aluno
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        aluno = Aluno.objects.create(user=user, **validated_data)
        return aluno

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            user_data = validated_data.pop('user')

            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
