from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from handy.models import Product

class WishList(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(
		'handy.Product',
		models.SET_NULL,
		blank=True,
		null=True,
		)

	