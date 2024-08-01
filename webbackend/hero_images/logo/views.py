from rest_framework import viewsets
from .models import Logo
from .serializers import LogoSerializer

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
