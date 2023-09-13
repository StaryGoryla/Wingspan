from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<str:room_name>/", views.room, name="room"),
]