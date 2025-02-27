from rest_framework import viewsets
from core.escola.models import Escola
from core.escola.serializers.escola import EscolaSerializer

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
