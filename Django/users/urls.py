from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("admin/", admin.site.urls),
    path("login_gui/", views.login_gui, name="login_gui"),
    path('register_gui/', views.register_gui, name="register_gui"),
    path('logout_gui/', views.logout_gui, name="logout_gui")
]