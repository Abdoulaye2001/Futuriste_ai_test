from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import SiteConfiguration

@receiver(post_migrate)
def create_site_configuration(sender, **kwargs):
        if not SiteConfiguration.objects.exists():
             SiteConfiguration.objects.create(coming_soon_active=False)