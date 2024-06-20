from django.db import models
from django.utils import timezone 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    body = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title

