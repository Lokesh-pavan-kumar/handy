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
    profile_pic = models.ImageField(default='default.png')
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    order_date = models.DateField()
    order_cost = models.IntegerField()


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
