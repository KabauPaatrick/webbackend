# serializers.py
from rest_framework import serializers
from .models import HomeView

class HomeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeView
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # No need to alter the image URL
        return representation
