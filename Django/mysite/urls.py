from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('users/', include('users.urls')),
]
