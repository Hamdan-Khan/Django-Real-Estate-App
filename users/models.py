# models
from django.db import models
from django.contrib.auth.models import AbstractUser
# auto save
from django.db.models.signals import post_save
from django.dispatch import receiver
# storage
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def profile_pic_path(instance, filename):
    return os.path.join('profile_pics', filename)


class CustomUser(AbstractUser):
    Gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(
        max_length=1, choices=Gender_choices, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True,)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to=profile_pic_path, blank=True,)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
