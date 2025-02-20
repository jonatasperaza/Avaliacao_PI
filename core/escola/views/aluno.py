from rest_framework import viewsets
from core.escola.modelosteste import Aluno
from core.escola.serializers.alunos import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
