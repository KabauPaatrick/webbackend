# locations/serializers.py
from rest_framework import serializers
from .models import Location, DropOffPoint

class DropOffPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropOffPoint
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    drop_off_points = DropOffPointSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'parent', 'children', 'drop_off_points')

    def get_children(self, obj):
        # Retrieve children locations
        children = obj.get_children()
        # Serialize children locations using the same serializer
        serializer = LocationSerializer(children, many=True)
        return serializer.data
