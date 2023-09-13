from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .forms import CustomUserCreation
from .models import CustomUser


def active(request):
    online_users = CustomUser.objects.filter(is_online=True)
    context = {'online_users': online_users}
    return render(request, 'active.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created!")
            return redirect('login')
    else:
        form = CustomUserCreation()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user.is_online)
        if user is not None:
            auth_login(request, user)
            user = CustomUser.objects.get(username=username)
            user.is_online = True
            user.save()
            print(user.is_online)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        user = request.user
        user.is_online = False
        user.save()
        auth_logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('home')


@api_view(['GET', 'POST'])
def logout_gui(request):
    auth_logout(request)
    return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def login_gui(request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def register_gui(request, *args, **kwargs):
    username = request.data.get('username')
    email = request.data.get('email')
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')
    if password1 != password2:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        form = CustomUserCreation(request.data)
        if form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
