from django.db import models
import uuid

class ChatMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_incoming = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.message_content}"
