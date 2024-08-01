from rest_framework import serializers
from .models import Entity

class EntitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  # Add this line

    class Meta:
        model = Entity
        fields = ['id', 'name', 'description', 'location', 'contact_person', 'email', 'phone_number']
