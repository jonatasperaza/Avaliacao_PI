from rest_framework import viewsets
from core.escola.modelosteste import Turma
from core.escola.serializers.turma import TurmaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
