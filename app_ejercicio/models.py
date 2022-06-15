from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
import json

class Redirect (models.Model):
    key = models.CharField(max_length=25)
    url = models.URLField()
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Redirect, )
def guardar_en_cache (sender, instance, **kwargs):
    if instance.active:
        datos = {
            "key" : instance.key,
            "url" : instance.url,
        }
        cache.set(instance.key, json.dumps(datos) , 60*60*60)
        return     


