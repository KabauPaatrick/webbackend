import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Creating user: {instance.username}")
        subject = 'Welcome to Our Platform'
        message = f'Hi {instance.username},\n\nThank you for registering on our platform.\n\nBest regards,\n Mama Jay Collection'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            logger.info(f"Welcome email sent to {instance.email}")
        except Exception as e:
            logger.error(f"Error sending email: {e}")
