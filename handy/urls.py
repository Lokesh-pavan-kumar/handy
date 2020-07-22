from django.urls import path
from .views import ProductDetailView, ArtisanDetailView, Ordersview
from . import views
from django.conf.urls import include

# from handy import views as handy_views

# app_name="handy-home"
urlpatterns = [
    path('', views.home, name="handy-home"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('artisan/<int:pk>/', ArtisanDetailView.as_view(), name="artisan-detail"),
    path('orders/', Ordersview, name="orders"),
    path('cart/<int:pk>/', views.cartview, name="cart"),
    path('del_cart/<int:pk>/', views.del_cartview, name="del_cart"),
    path('update_cart/', views.update_cartview, name="update_cart"),
    path('update_rating/', views.update_ratingview, name="update_rating"),
    path('update_review/', views.update_reviewview, name="update_review"),
    path('get_reviews/', views.get_reviewsview, name="get_reviews"),
    path('cart/', views.cart, name="cartit"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('cart/checkout/', views.Checkout, name="checkout"),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
