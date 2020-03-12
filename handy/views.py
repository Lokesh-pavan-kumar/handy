from django.shortcuts import render
from .models import Product, Category, Artisan
from django.views.generic import ListView, DetailView


def home(request):
    products = {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'handy/home.html', products)


class ProductDetailView(DetailView):
    model = Product

class ArtisanDetailView(DetailView):
	model = Artisan