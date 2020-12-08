from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # Home Pages

    path('',views.index,name='home'),
    path('about', views.about, name='about'),
    path('package', views.package, name='package'),
    path('contact', views.contact, name='contact'),
    path('register_signin', views.register_signin, name='register_signin'),

    # Places
    
    path('paris', views.paris, name='paris'),
    path('cyprus', views.cyprus, name='cyprus'),
    path('los_angeles', views.los_angeles, name='los_angeles'),
    path('venice', views.venice, name='venice'),
    path('prague', views.prague, name='prague'),
    path('tokyo', views.tokyo, name='tokyo'),
    
]