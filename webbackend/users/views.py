from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        serializer.save()
