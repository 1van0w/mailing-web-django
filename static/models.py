from django.db import models
from mailings.models import Mailing

class MailingStatistics(models.Model):
    mailing = models.OneToOneField(Mailing, on_delete=models.CASCADE, primary_key=True)
    sent_messages = models.IntegerField(default=0)
    successful_deliveries = models.IntegerField(default=0)

    def __str__(self):
        return f"Statistics for Mailing {self.mailing.unique_id}"
