from django.db import models

# Create your models here.
from django.db import models

class ChatMessage(models.Model):
    user_message = models.TextField()
    sentiment = models.CharField(max_length=20)
    confidence = models.FloatField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_message} -> {self.sentiment}"