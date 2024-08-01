from rest_framework import serializers
from .models import HeroPage

class HeroPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroPage
        fields = ['id', 'title', 'description', 'ctatext', 'entity', 'image']

    def create(self, validated_data):
        # Extract and remove the 'image' field from the validated data
        image_file = validated_data.pop('image', None)
        
        # Create the HeroPage instance without saving it to the database yet
        hero_page = HeroPage.objects.create(**validated_data)

        # If an image was provided, save it to the hero_images directory
        if image_file:
            hero_page.image.save(image_file.name, image_file, save=True)

        return hero_page
