import logging
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

logger = logging.getLogger(__name__)

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # Ensure this matches the primary key field in your model

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        logger.info(f"Attempting to delete user with ID: {kwargs['pk']}")
        response = super().destroy(request, *args, **kwargs)
        logger.info(f"User with ID: {kwargs['pk']} successfully deleted")
        return response
