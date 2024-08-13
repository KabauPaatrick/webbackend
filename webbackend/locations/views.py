# locations/views.py
from rest_framework import viewsets
from .models import Location, DropOffPoint
from .serializers import LocationSerializer, DropOffPointSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DropOffPointViewSet(viewsets.ModelViewSet):
    queryset = DropOffPoint.objects.all()
    serializer_class = DropOffPointSerializer
