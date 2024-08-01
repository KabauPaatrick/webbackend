# FileUpload/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FileUploadSerializer
from .models import UploadedFile

class FileUploadViewSet(viewsets.ViewSet):
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_files = serializer.save()
            return Response({
                'success': True,
                'data': uploaded_files,
                'message': 'Files uploaded successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
