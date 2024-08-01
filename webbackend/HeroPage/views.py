from rest_framework import viewsets
from .models import HeroPage
from .serializers import HeroPageSerializer

class HeroPageViewSet(viewsets.ModelViewSet):
    queryset = HeroPage.objects.all()
    serializer_class = HeroPageSerializer
