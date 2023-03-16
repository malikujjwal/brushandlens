from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.TextField()

class Images(models.Model):
    title = models.CharField(max_length=256)
    image_path = models.CharField(max_length=260)
    price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Likes(models.Model):
    image_path = models.CharField(max_length=260)
    user = models.ForeignKey(User, on_delete=models.CASCADE)