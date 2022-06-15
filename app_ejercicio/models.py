from django.db import models

class Redirect (models.Model):
    key = models.CharField(max_length=25)
    url = models.URLField()
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
