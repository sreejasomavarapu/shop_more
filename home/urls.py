from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.list,name='home'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='home/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='home/logout.html'),name='logout'),
    path('detail/',views.detail),
    path('about/',views.about,name='about')
]