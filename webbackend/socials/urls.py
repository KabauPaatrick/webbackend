from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageDetailView, IncomingChatMessagesView

urlpatterns = [
    path('messages/', ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
    path('messages/<int:pk>/', ChatMessageDetailView.as_view(), name='chat-message-detail'),
    path('incoming-messages/', IncomingChatMessagesView.as_view(), name='incoming-chat-messages'),
]
