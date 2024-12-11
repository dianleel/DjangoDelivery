# main/views.py

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

@login_required
def orders_view(request):
    return render(request, 'main/orders.html')

def about_view(request):
    return render(request, 'main/about.html')

def faq_view(request):
    return render(request, 'main/faq.html')

def index(request):
    popular_spots = [
        {
            'logo': 'images/magnum.jpg',
            'name': 'Magnum',
            'description': 'Продукты и не только'
        },
        {
            'logo': 'images/pharmacy.jpeg',
            'name': 'Садыхан',
            'description': 'Лучшие цены в Алматы'
        },
        {
            'logo': 'images/bahandi-logo.jpg',
            'name': 'Bahandi',
            'description': 'Эти бургеры не нуждаются в рекламе'
        }
    ]
    return render(request, 'main/index.html', {'popular_spots': popular_spots})