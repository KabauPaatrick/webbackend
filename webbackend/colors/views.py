# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Color
from .serializers import ColorSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "success": True,
            "data": serializer.data,
            "message": "Color created successfully"
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


# Create your views here.
