from django.urls import path
from . import views
from .views import WishListView

urlpatterns = [
    path('<int:pk>/', views.add_to_wishlist, name="add_to_wishlist"),
    path('', WishListView.as_view(), name="wishlist"),
    path('remove/<int:pk>', views.del_from_wishlist, name="del_from_wishlist")
]
