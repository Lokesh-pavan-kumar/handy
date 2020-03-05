
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customers import views as customer_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='customer-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customers/logout.html'), name='customer-logout'),
    path('', include('handy.urls')),
    path('register/', customer_views.register, name='customer-register'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

