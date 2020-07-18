
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search),
    path('filter/<str:category>', views.filter)
]
