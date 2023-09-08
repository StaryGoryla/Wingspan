from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreation
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)