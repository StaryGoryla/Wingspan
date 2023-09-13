from django.db import models
from users.models import CustomUser

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

class ChatMessage(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)