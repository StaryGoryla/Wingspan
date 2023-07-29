from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html", {'name': 'buzdygan'})


def game(request):
    return render(request, "game.html")


def stats(request):
    return render(request, "stats.html")


@login_required()
def profile(request):
    return render(request, "profile.html")