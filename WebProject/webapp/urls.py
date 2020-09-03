from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about_us', views.about, name='about_us'),
    path('services', views.services, name='services'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
