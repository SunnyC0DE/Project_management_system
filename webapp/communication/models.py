from django.db import models
from items.models import Items
from django.contrib.auth.models import User

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Items, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User , related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_message', on_delete=models.CASCADE)