from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Member, ProviderMember
import folium
from django.db import models
import requests
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], 
                        password=request.POST['password'],  firstname=request.POST['firstname'], 
                        lastname=request.POST['lastname'],email=request.POST['email'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'templates/register.html')
    
def providerIndex(request):
    if request.method == 'POST':
        member = ProviderMember(username=request.POST['username'], 
                        password=request.POST['password'],  firstname=request.POST['firstname'], 
                        lastname=request.POST['lastname'],email=request.POST['email'],category=request.POST['category'],
                        phone=request.POST['phone'],experience=request.POST['experience'])
        member.save()
        return redirect('/providerLogin')
    else:
        return render(request, 'templates/providerRegister.html')

def firstPage(request):
    return render(request, 'firstPage.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def providerLogin(request):
    return render(request, 'provider_login.html')

def providerRegister(request):
    return render(request, 'provider_register.html')

def home(request):
    if request.method == 'POST':
        member = Member.objects.get(id = request.POST['profile'])
        return render(request, 'home.html', {'member': member})

def map(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])

            # key='lNJ01Y07OWmENByHWsdfyU2A0jIVL3Gh'
            # url = 'https://www.mapquestapi.com/geocoding/v1/address?key='
            # loc = 'Mirpur,Dhaka'
            # main = url+key+'&location='+loc
            # r = requests.get(main)
            # data =r.json()['results'][0]
            # location = data['locations'][0]

            # latitude = location['latLng']['lat']
            # longitude = location['latLng']['lng']


            
            # ip_address = request.META.get('REMOTE_ADDR')
            # print(ip_address)

            # # Call the ipapi API to get the user's location
            # url = f'http://ipapi.co/{ip_address}/json/'
            # response = requests.get(url)
            # location_data = response.json()
            # print(location_data)

            # latitude = location_data.get('latitude')
            # longitude = location_data.get('longitude')
            # response = requests.get('https://api.ipify.org?format=json')
            # ip_address = response.json()['ip']

            # # Send a request to the Google Maps Geocoding API
            # url = 'https://maps.googleapis.com/maps/api/geocode/json'
            # params = {
            #     'address': ip_address,
            #     'key': 'AIzaSyACxuyBwxbn341tVqacATywUMADhgw-Nmw'
            #         }
            # response = requests.get(url, params=params).json()

            # # Extract the latitude and longitude from the response
            # # print(response['results'])
            # # location = response['results'][0]['geometry']['location']
            # # latitude = location['lat']
            # # longitude = location['lng']

            # # Print the latitude and longitude
            # # print('Latitude:', latitude)
            # # print('Longitude:', longitude)





            # # ip = requests.get('https://api.ipify.org?format=json')
            # # ip_data = json.loads(ip.text)
            # # res = requests.get('http://ip-api.com/json/45.118.63.58')
            # # print(ip_data["ip"])
            # # location_data = json.loads(res.text)

            m = folium.Map(location=[23.69, 90.9])
            folium.Marker([23.804500579833984, 90.36070251464844],tooltip='Click for more info', popup=member.username).add_to(m)
            folium.Marker([23.88, 90.4],tooltip='Click for more info', popup='<strong><h4>Masum<h4></strong><br>Category: Electrician<br>Experience: 5 Years',icon = folium.Icon(color='red')).add_to(m)
            folium.Marker([23.96, 89.7],tooltip='Click for more info', popup='<strong><h4>Fahad<h4></strong><br>Category: Electrician<br>Experience: 10 Years',icon = folium.Icon(color='red')).add_to(m)
            folium.Marker([23.88, 89.8],tooltip='Click for more info', popup='<strong><h4>Shawon<h4></strong><br>Category: Plumber<br>Experience: 2 Years',icon = folium.Icon(color='red')).add_to(m)
            folium.Marker([23.90, 89.99],tooltip='Click for more info', popup='<strong><h4>Monir<h4></strong><br>Category: Plumber<br>Experience: 5 Years',icon = folium.Icon(color='red')).add_to(m)
            folium.Marker([23.82, 90.16],tooltip='Click for more info', popup='<strong><h4>Ferdous<h4></strong><br>Category: Electrician<br>Experience: 7 Years',icon = folium.Icon(color='red')).add_to(m)
            folium.Marker([23.99, 90.3],tooltip='Click for more info', popup='<strong><h4>Rubel<h4></strong><br>Category: Carpenter<br>Experience: 2 Years',icon = folium.Icon(color='red')).add_to(m)
            m = m._repr_html_()
            context = {
                'm' : m,
                'member': member,
            }
            return render(request, 'map.html', context)
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
