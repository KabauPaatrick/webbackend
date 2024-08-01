from rest_framework import serializers
from .models import Product, ProductImage
import cloudinary.uploader

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'file', 'asset_id', 'public_id']
        read_only_fields = ['id', 'asset_id', 'public_id']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    tags = serializers.JSONField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'slug', 'price', 'category', 'brand', 
            'quantity', 'sold', 'colors', 'image', 'tags', 'total_ratings', 
            'ratings', 'created_at', 'updated_at', 'images', 'image_files'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total_ratings', 'ratings']

    def create(self, validated_data):
        image_files = validated_data.pop('image_files', [])
        tags = validated_data.pop('tags', None)  # Handle case where tags might be None
        colors = validated_data.pop('colors', [])

        # Handle CloudinaryField for main product image
        image = validated_data.pop('image', None)

        # Create the product instance
        product = Product.objects.create(**validated_data, tags=tags, image=image)

        product.colors.set(colors)

        # Create ProductImage instances for additional images
        for image_file in image_files:
            ProductImage.objects.create(product=product, file=image_file)

        return product

    def update(self, instance, validated_data):
        image_files = validated_data.pop('image_files', [])
        tags = validated_data.pop('tags', None)  # Handle case where tags might be None

        # Update fields on the product instance
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.sold = validated_data.get('sold', instance.sold)
        instance.colors.set(validated_data.get('colors', instance.colors))
        instance.tags = tags  # Update tags field

        # Handle CloudinaryField for main product image
        instance.image = validated_data.get('image', instance.image)

        instance.save()

        # Create or update ProductImage instances for additional images
        for image_file in image_files:
            ProductImage.objects.create(product=instance, file=image_file)

        return instance

    def delete(self, instance):
        # Delete images from Cloudinary
        for image in instance.images.all():
            cloudinary.uploader.destroy(image.public_id)
            image.delete()

        # Delete the product instance
        instance.delete()
