# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model

# class EmailOrUsernameModelBackend(object):
#     def authenticate(self, username=None, password=None):
#         if '@' in username:
#             kwargs = {'email': username}
#         else:
#             kwargs = {'username': username}
#         try:
#             user = get_user_model().objects.get(**kwargs)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, username):
#         try:
#             return get_user_model().objects.get(pk=username)
#         except get_user_model().DoesNotExist:
#             return None

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    Door_flat = models.CharField(max_length=100, blank=True)
    Street = models.CharField(max_length=100, blank=True)
    City = models.CharField(max_length=100, blank=True)
    State = models.CharField(max_length=100, blank=True)
    Country = models.CharField(max_length=100, blank=True)
    Pincode = models.CharField(max_length=100, blank=True)
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



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
