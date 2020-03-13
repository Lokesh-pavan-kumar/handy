from django.db import models
from django.utils import timezone

class Artisan(models.Model):
	name = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	address = models.TextField()
	birthday = models.DateField()

	def __str__(self):
		return self.name

class Category(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class Product(models.Model):
	artisan_id = models.ForeignKey(
		'Artisan',
		models.SET_NULL,
		blank=True,
		null=True,
		)
	name = models.CharField(max_length=100)
	category = models.ForeignKey(
		'Category',
		models.SET_NULL,
		blank=True,
		null=True,
		)
	date_posted = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default='default.jpg', upload_to='thumbnail_pics')
	last_modified = models.DateTimeField(auto_now=True)
	price = models.FloatField()
	description = models.TextField()
	availability = models.BooleanField(default=False)

	def __str__(self):
		return self.name

