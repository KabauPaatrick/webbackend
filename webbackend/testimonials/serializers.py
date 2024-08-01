from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  

    class Meta:
        model = Testimonial
        fields = '__all__'
