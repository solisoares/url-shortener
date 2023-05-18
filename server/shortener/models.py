from datetime import datetime

from django.db import models
from django.db.models import F

import hashids


hash_creator = hashids.Hashids(salt="42", min_length=5)


# Create your models here.
class URL(models.Model):
    original_url = models.URLField(unique=True, max_length=200)
    short_url = models.CharField(unique=True, max_length=5, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_access_datetime = models.DateTimeField(null=True)
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """Overrides save by automatically creating and saving the short url"""
        is_new = not self.pk  # self.pk is initialized after DB insertion
        super().save(*args, **kwargs)  # regular saving process

        if is_new:
            self.short_url = hash_creator.encode(self.pk)
            super().save(update_fields=["short_url"])

    def update_last_access(self):
        self.access_count = F("access_count") + 1
        self.last_access_datetime = datetime.now()
        self.save()
