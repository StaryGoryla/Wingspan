from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
import json
from django.http import JsonResponse
from users.models import CustomUser


def home(request):
    online_users = CustomUser.objects.filter(is_online=True)
    context = {'online_users': online_users}
    return render(request, "home.html", context)


def game(request):
    return render(request, "game.html")


def stats(request):
    return render(request, "stats.html")


@login_required()
def profile(request):
    return render(request, "profile.html")

