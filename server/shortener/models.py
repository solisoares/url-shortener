from django.db import models

import hashids

# Create your models here.
class URL(models.Model):
    original_url = models.URLField(unique=True, max_length=200)
    short_url = models.CharField(unique=True, max_length=5, blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_access_datetime = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """Overrides save by automatically creating and saving the short url"""
        is_new = not self.pk  # self.pk is initialized after DB insertion
        super().save(*args, **kwargs)  # regular saving process

        if is_new:
            self.short_url = self._hash_url()
            super().save(update_fields=["short_url"])

    def _hash_url(self):
        hashid = hashids.Hashids(salt="42", min_length=5)
        return hashid.encode(self.pk)