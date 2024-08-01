from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def perform_create(self, serializer):
        serializer.save()

class ChatMessageDetailView(generics.RetrieveAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class IncomingChatMessagesView(APIView):
    def get(self, request, *args, **kwargs):
        incoming_messages = ChatMessage.objects.filter(is_incoming=True)
        serializer = ChatMessageSerializer(incoming_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
