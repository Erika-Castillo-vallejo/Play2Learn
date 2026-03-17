from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    ACCOUNT_TYPES = [
        ("personal", "Personal"),
        ("business", "Business"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20, blank=True)

    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES,
        default="personal"
    )

    age = models.IntegerField(null=True, blank=True)

    referrer = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Crear automáticamente el Profile cuando se crea un usuario
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Guardar Profile cuando se guarda User
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()