from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
import json
from django.http import JsonResponse


def home(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    logged_in_users = []
    for session in sessions:
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if user_id:
            user = User.objects.get(id=user_id)
            logged_in_users.append(user)
    return render(request, "home.html", {'logged_in_users': logged_in_users})


def game(request):
    return render(request, "game.html")


def stats(request):
    return render(request, "stats.html")


@login_required()
def profile(request):
    return render(request, "profile.html")

