from rest_framework import serializers
from .models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Add this line

    class Meta:
        model = Achievement
        fields = '__all__'
