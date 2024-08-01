from rest_framework import viewsets
from .models import HomeView
from .serializers import HomeViewSerializer

class HomeViewViewSet(viewsets.ModelViewSet):
    queryset = HomeView.objects.all()
    serializer_class = HomeViewSerializer
    lookup_field = 'id' 
