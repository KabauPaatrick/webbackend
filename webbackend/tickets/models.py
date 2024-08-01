import uuid
from django.db import models
from customer.models import Customer

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('InProgress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='ticket_attachments/', null=True, blank=True)  # New field for attachments

    def __str__(self):
        return f"Ticket {self.id} - {self.subject}"
