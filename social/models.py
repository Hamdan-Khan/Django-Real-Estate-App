from django.db import models
from market.models import Property
from users.models import CustomUser
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sender_messages", blank=True, null=True)
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reciever_messages", blank=True, null=True)
    sender_name = models.CharField(max_length=200, blank=True, null=True)
    sender_email = models.EmailField(blank=True, null=True)
    sender_number = models.CharField(max_length=15, blank=True, null=True)
    message_text = models.TextField(blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name="property_messages", blank=True, null=True)
    sent_at = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.message_text
