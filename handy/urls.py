
from django.urls import path
from .views import ProductDetailView, ArtisanDetailView
from . import views
#from handy import views as handy_views

# app_name="handy-home"
urlpatterns = [
    path('', views.home, name="handy-home"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('artisan/<int:pk>/', ArtisanDetailView.as_view(), name="artisan-detail"),
    path('cart/<int:pk>/',views.cartview,name="cart"),
    path('del_cart/<int:pk>/',views.del_cartview,name="del_cart"),
    path('update_cart/',views.update_cartview,name="update_cart"),
    path('cart/',views.cart,name="cartit"),
]

