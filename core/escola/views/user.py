from rest_framework import viewsets
from core.escola.modelosteste import User
from core.escola.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
