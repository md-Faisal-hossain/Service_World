from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', firstPage, name='firstPage'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('providerLogin', providerLogin, name='providerLogin'),
    path('providerRegister', providerRegister, name='providerRegister'),
    path('index', index, name='index'),
    path('providerIndex', providerIndex, name='providerIndex'),
    path('map', map, name='map'),
    path('home', home, name='home'),
]