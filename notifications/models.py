from django.db import models
from accounts.models import Profile

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
