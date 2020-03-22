from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Address
from handy.models import Product

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_ordered = models.DateTimeField(auto_now_add=True)

	product_price = models.FloatField()
	delivery_price = models.FloatField()
	net_price = models.FloatField()

	address = models.OneToOneField(
		'accounts.Address',
		models.SET_NULL,
		blank=True,
		null=True,
		)

	product = models.OneToOneField(
		'handy.Product',
		models.SET_NULL,
		blank=True,
		null=True,
		)

	quantity = models.IntegerField(default=0)

