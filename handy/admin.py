from django.contrib import admin
from .models import Artisan, Product, Category, Cart

admin.site.register(Artisan)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)