from django.db import models
from django.utils import timezone

# Create your models here.
# class ArtWork():
#     title = models.CharField(max_length=256)
#     theme = models.CharField(max_length=256)
#     image_path = models.CharField(max_length=260)
#     date_posted = models.DateTimeField(default=timezone.now)
#     artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
#     likes = models.IntegerField(blank=True, null=True)
#     price = models.IntegerField()

# class Artist():
#     name = models.CharField(max_length=256)
#     description = models.TextField()