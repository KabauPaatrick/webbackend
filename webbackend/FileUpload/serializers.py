# FileUpload/serializers.py
from rest_framework import serializers
from cloudinary.uploader import upload

from .models import UploadedFile

class FileUploadSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.FileField(max_length=100000, allow_empty_file=False))
    model_type = serializers.CharField()

    def create(self, validated_data):
        uploaded_files = []
        model_type = validated_data['model_type']

        for file in validated_data['files']:
            try:
                # Upload file to Cloudinary
                upload_data = upload(file)
                
                # Create UploadedFile instance in database
                uploaded_file = UploadedFile.objects.create(
                    file=file,
                    asset_id=upload_data['asset_id'],
                    public_id=upload_data['public_id'],
                    model_type=model_type
                )
                
                # Append uploaded file details to response
                uploaded_files.append({
                    'id': uploaded_file.id,
                    'file_url': upload_data['secure_url'],
                    'asset_id': upload_data['asset_id'],
                    'public_id': upload_data['public_id']
                })
            
            except Exception as e:
                # Handle any exceptions during upload or database creation
                uploaded_files.append({
                    'error': f'Failed to upload file: {str(e)}'
                })

        return uploaded_files
