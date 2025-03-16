from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Organization

@receiver(post_save, sender=Organization)
def log_organization_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Organization {instance.name} created.")

@receiver(post_delete, sender=Organization)
def log_organization_deletion(sender, instance, **kwargs):
    print(f"Organization {instance.name} deleted.")
