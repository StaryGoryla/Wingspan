from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("home/", views.home, name="home"),
    path("game/", views.game, name="game"),
    path("stats/", views.stats, name="stats"),
    path("profile/", views.profile, name="profile"),
    path("admin/", admin.site.urls),
]