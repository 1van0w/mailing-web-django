from django.db import models

class Notification(models.Model):
    text = models.TextField()
    status = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Notification {self.id}"
