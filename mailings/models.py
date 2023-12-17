from django.db import models
from django.utils import timezone
import uuid

class Client(models.Model):
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=12, unique=True)  # Формат 7XXXXXXXXXX
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f"Client {self.unique_id}"

class Message(models.Model):
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_datetime = models.DateTimeField(default=timezone.now)
    sending_status = models.CharField(max_length=50)
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message {self.unique_id}"

class Mailing(models.Model):
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    message_text = models.TextField()
    client_properties = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Mailing {self.unique_id}"