from django.shortcuts import render
from .models import Product, Category

def home(request):

	products = {
		'thumbnails' : Product.objects.all(),
		'category' : Category.objects.all()  
	}
	return render(request, 'handy/home.html', products)
