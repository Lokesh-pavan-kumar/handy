# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    address = models.TextField(blank=True)
    profile_pic = models.ImageField(default='default.jpg')

    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def set_image_to_default(self):
        self.profile_pic.delete(save=False)  # delete old image file
        self.profile_pic = 'default.jpg'
        self.save()


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
