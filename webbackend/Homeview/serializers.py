from rest_framework import serializers
from .models import HomeView

class HomeViewSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = HomeView
        fields = ['id', 'title', 'description', 'ctatext', 'entity', 'image']
