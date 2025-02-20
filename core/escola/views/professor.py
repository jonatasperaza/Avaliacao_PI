from rest_framework import viewsets
from core.escola.modelosteste import Professor
from core.escola.serializers.professores import ProfessorSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
