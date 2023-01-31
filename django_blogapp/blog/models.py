from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """Model describing a blog post"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ''+self.title