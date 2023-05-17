from django.db import models


# Create your models here.
class URL(models.Model):
    original_url = models.URLField(unique=True, max_length=200)
    short_url = models.CharField(unique=True, max_length=5)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_access_datetime = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)
