from rest_framework import viewsets
from .models import Achievement
from .serializers import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    lookup_field = 'id' 
