import uuid
from django.db import models
from tickets.models import Ticket  # Assuming the Ticket model is in the 'tickets' app

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(Account, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} on Ticket {self.ticket.ticketId}"
