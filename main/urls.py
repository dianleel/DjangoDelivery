# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('orders/', views.orders_view, name='orders'),
    path('profile/', views.profile_view, name='profile'),
    path('faq/', views.faq_view, name='faq'),
]