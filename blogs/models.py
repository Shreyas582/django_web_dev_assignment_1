from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    blog_title = models.CharField(max_length=256, blank=True, default='')
    content = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering = ['created_at']
