# serializers.py
from rest_framework import serializers
from .models import Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'created_at', 'updated_at']
