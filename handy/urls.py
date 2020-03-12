
from django.urls import path
from .views import ProductDetailView, ArtisanDetailView
from . import views

urlpatterns = [
    path('', views.home, name="handy-home"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('artisan/<int:pk>/', ArtisanDetailView.as_view(), name="artisan-detail")
]


