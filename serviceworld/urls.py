from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', firstPage, name='firstPage'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('edit', edit, name='edit'),
    path('providerEdit', providerEdit, name='providerEdit'),
    path('updateProfile', updateProfile, name='updateProfile'),
    path('updateProviderProfile', updateProviderProfile, name='updateProviderProfile'),
    path('providerLogin', providerLogin, name='providerLogin'),
    path('providerRegister', providerRegister, name='providerRegister'),
    path('providerProfile/<int:id>', providerProfile, name='providerProfile'),
    path('index', index, name='index'),
    path('providerIndex', providerIndex, name='providerIndex'),
    path('providerCheck', providerCheck, name='providerCheck'),
    path('providerHome', providerHome, name='providerHome'),
    path('providerMap', providerMap, name='providerMap'),
    path('providerMapOn', providerMapOn, name='providerMapOn'),
    path('providerAccept', providerAccept, name='providerAccept'),
    path('request', request, name='request'),
    path('map', map, name='map'),
    path('check', check, name='check'),
    path('connection', connection, name='connection'),
    path('searchProvider', searchProvider, name='searchProvider'),
    path('home', home, name='home'),
]