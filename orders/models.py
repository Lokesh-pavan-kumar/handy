from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Address
from handy.models import Product


class Map(models.Model):
    ord_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    start = models.IntegerField()
    count = models.IntegerField()
    amount = models.FloatField(default=0.0)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=1111)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    product = models.ForeignKey(
        'handy.Product',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    quantity = models.IntegerField(default=0)
    net_price = models.FloatField(default=0.0)
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True)
    order_status = models.CharField(max_length=10, default="Delivered", choices=[
        ('Processing', 'Processing'),
        ('Recieved', 'Recieved'),
        ('Waiting', 'Waiting'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ])

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_ordered = models.DateTimeField(auto_now_add=True)
    #
    # product_price = models.FloatField()
    # delivery_price = models.FloatField()
    # net_price = models.FloatField()
    #
    # address = models.OneToOneField(
    #     'accounts.Address',
    #     models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )
    #
    # product = models.OneToOneField(
    #     'handy.Product',
    #     models.SET_NULL,
    #     blank=True,
    #     null=True,
    # )
    #
    # quantity = models.IntegerField(default=0)
