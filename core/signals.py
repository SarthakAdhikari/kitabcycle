from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import User, Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from . import signals #NOQA
