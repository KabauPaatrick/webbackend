from rest_framework import serializers
from .models import Logo

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['id', 'entity', 'image']

    def create(self, validated_data):
        # Extract and remove the 'image' field from the validated data
        image_file = validated_data.pop('image', None)
        
        # Create the Logo instance without saving it to the database yet
        logo =logo.objects.create(**validated_data)

        # If an image was provided, save it to the hero_images directory
        if image_file:
            logo.image.save(image_file.name, image_file, save=True)

        return logo