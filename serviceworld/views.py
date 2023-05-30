from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Member, ProviderMember, ConnectionRequest
import folium
from django.db import models
import requests
import json




# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES.get('img'):
        send_url = "http://api.ipstack.com/check?access_key=bf03f5d6cb8843da287d2c1e40714ba1"
        geo_req = requests.get(send_url)
        print(geo_req)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        member = Member(username=request.POST['username'], 
                        password=request.POST['password'],  firstname=request.POST['firstname'], 
                        lastname=request.POST['lastname'],email=request.POST['email'],lat=latitude,lng=longitude,image=request.FILES['img'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'templates/register.html')
    
def providerIndex(request):
    if request.method == 'POST':
        send_url = "http://api.ipstack.com/check?access_key=bf03f5d6cb8843da287d2c1e40714ba1"
        geo_req = requests.get(send_url)
        print(geo_req)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        member = ProviderMember(username=request.POST['username'], 
                        password=request.POST['password'],  firstname=request.POST['firstname'], 
                        lastname=request.POST['lastname'],email=request.POST['email'],category=request.POST['category'],
                        phone=request.POST['phone'],experience=request.POST['experience'],lat=latitude,lng=longitude,image=request.FILES['img'])
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


def providerProfile(request,id):
    member = ProviderMember.objects.get(id=id)
    context = {
                'member': member,
            }
    return render(request,'provider_profile.html',context)

def check(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            global val
            def val():
                return member
            return redirect(map)
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)


def providerCheck(request):
    if request.method == 'POST':
        if ProviderMember.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = ProviderMember.objects.get(username=request.POST['username'], password=request.POST['password'])
            global pval
            def pval():
                return member
            return redirect(providerMap)
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'provider_login.html', context)


def home(request):
    if request.method == 'POST':
        member = Member.objects.get(id = request.POST['profile'])
        return render(request, 'home.html', {'member': member})

def map(request):
            
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
    member=val()
    m = folium.Map(location=[23.69, 90.360702])
    folium.Marker([member.lat,member.lng]).add_to(m)
    PMember = ProviderMember.objects.all()
    for pmember in PMember:
        html = folium.Html(
                        f"""
                        <!DOCTYPE html>
                        <html>
                        <body>
                        <img style="border: 1px solid #ddd;border-radius: 4px;padding: 5px;width: 150px;display: block;margin-left: auto;margin-right: auto;" src="{ pmember.image.url }" alt="Image">
                        <table class="table">
                        <thead class="thead-light">
                        <tr>
                            <th scope="col">First Name</th>
                            <th scope="col">{pmember.firstname}</th>
                        </tr>
                        <tr>
                            <th scope="col">Last Name</th>
                            <th scope="col">{pmember.lastname}</th>
                        </tr>
                        <tr>
                            <th scope="col">Email</th>
                            <th scope="col">{pmember.email}</th>
                        </tr>
                        <tr>
                            <th scope="col">Category</th>
                            <th scope="col">{pmember.category}</th>
                        </tr>
                        <tr>
                            <th scope="col">Experience</th>
                            <th scope="col">{pmember.experience}</th>
                        </tr>
                        <tr>
                            <th scope="col">Phone</th>
                            <th scope="col">{pmember.phone}</th>
                        </tr>
                        </thead>
                        </tbody>
                        </table>
                            <center><a href="providerProfile/{pmember.id}" target="_blank"><button style="background-color: blue;
                                            color: black;" class="btn btn-outline-success my-2 my-sm-0" type="submit"><strong>Profile</strong></button></a></center>
                        
                        </body>
                        </html>
                        """, 
                        script=True)
        popup  = folium.Popup(html, max_width=500)
        folium.Marker([pmember.lat, pmember.lng],tooltip='Click for more info', popup=popup,icon = folium.Icon(color='red')).add_to(m)

    m = m._repr_html_()
    context = {
        'm' : m,
        'member': member,
        }
    return render(request, 'map.html', context)
        
def connection(request):
    if request.method == 'POST':
        Pmember = ProviderMember.objects.get(id = request.POST['connection'])
        m = folium.Map(location=[23.69, 90.360702])
        member=val()
        folium.Marker([member.lat,member.lng]).add_to(m)
        html = folium.Html(
                        f"""
                        <!DOCTYPE html>
                        <html>
                        <body>
                        <table class="table">
                        <thead class="thead-light">
                        <tr>
                            <th scope="col">First Name</th>
                            <th scope="col">{Pmember.firstname}</th>
                        </tr>
                        <tr>
                            <th scope="col">Last Name</th>
                            <th scope="col">{Pmember.lastname}</th>
                        </tr>
                        <tr>
                            <th scope="col">Category</th>
                            <th scope="col">{Pmember.category}</th>
                        </tr>
                        <tr>
                            <th scope="col">Experience</th>
                            <th scope="col">{Pmember.experience}</th>
                        </tr>
                        </thead>
                        </tbody>
                        </table>
                            <center><a href="map" target="_blank"><button style="background-color: blue;
                                            color: black;" class="btn btn-outline-success my-2 my-sm-0" type="submit"><strong>Cancel</strong></button></a></center>
                        
                        </body>
                        </html>
                        """, 
                        script=True)
        popup  = folium.Popup(html, max_width=500)
        folium.Marker([Pmember.lat, Pmember.lng],tooltip='Click for more info', popup=popup,icon = folium.Icon(color='red')).add_to(m)
        folium.PolyLine([(23.804500579833984, 90.399070251464844),(Pmember.lat, Pmember.lng)]).add_to(m)
        m = m._repr_html_()
        connect = ConnectionRequest(mid=member.id,pid=Pmember.id)
        connect.save()
        context = {
                'm' : m,
                'member': member,
            }
        return render(request, 'map.html', context)
    
def searchProvider(request):
    if request.method == 'POST':
        type=request.POST['type']
        m = folium.Map(location=[23.69, 90.360702])
        member=val()
        folium.Marker([member.lat,member.lng]).add_to(m)
        PMember = ProviderMember.objects.all()
        for pmember in PMember:
            if pmember.category == type:
                html = folium.Html(
                                f"""
                                <!DOCTYPE html>
                                <html>
                                <body>
                                <img style="border: 1px solid #ddd;border-radius: 4px;padding: 5px;width: 150px;display: block;margin-left: auto;margin-right: auto;" src="{ pmember.image.url }" alt="Image">
                                <table class="table">
                                <thead class="thead-light">
                                <tr>
                                    <th scope="col">First Name</th>
                                    <th scope="col">{pmember.firstname}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Last Name</th>
                                    <th scope="col">{pmember.lastname}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Email</th>
                                    <th scope="col">{pmember.email}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Category</th>
                                    <th scope="col">{pmember.category}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Experience</th>
                                    <th scope="col">{pmember.experience}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Phone</th>
                                    <th scope="col">{pmember.phone}</th>
                                </tr>
                                </thead>
                                </tbody>
                                </table>
                                    <center><a href="providerProfile/{pmember.id}" target="_blank"><button style="background-color: blue;
                                                    color: black;" class="btn btn-outline-success my-2 my-sm-0" type="submit"><strong>Profile</strong></button></a></center>
                                </body>
                                </html>
                                """, 
                                script=True)
                popup  = folium.Popup(html, max_width=500)
                folium.Marker([pmember.lat, pmember.lng],tooltip='Click for more info', popup=popup,icon = folium.Icon(color='red')).add_to(m)
        m = m._repr_html_() 
        context = {
                    'm' : m,
                    'member': member,
                }
        return render(request, 'map.html', context)
    
def providerMap(request):
    m = folium.Map(location=[23.69, 90.360702])
    m = m._repr_html_()
    member=pval() 
    context = {
                    'm' : m,
                    'member': member,
                }
    return render(request, 'provider_map.html', context)

def providerMapOn(request):
    pmember=pval()
    m = folium.Map(location=[23.69, 90.360702])
    folium.Marker([pmember.lat, pmember.lng]).add_to(m)
    m = m._repr_html_() 
    context = {
                    'm' : m,
                    'member': pmember,
                }
    return render(request, 'provider_mapOn.html', context)

def providerHome(request):
    if request.method == 'POST':
        member = ProviderMember.objects.get(id = request.POST['profile'])
        return render(request, 'providerHome.html', {'member': member})
    
def request(request):
    pmember=pval()
    # member = []
    message = ConnectionRequest.objects.all()
    # for mes in message:
    #     if mes.pid == pmember.id:
    #         member.append(Member.objects.get(id = mes.mid))
    
    # global reqVal
    # def reqVal():
    #     return member

    context = {
                    'm' : message,
                    'pmember': pmember,
                    # 'member' : member,
                }
    return render(request, 'request.html',context)

def providerAccept(request):
    mid = request.POST['accept']
    member = Member.objects.get(id = mid)
    pmember=pval()
    m = folium.Map(location=[23.69, 90.360702])
    html = folium.Html(
                                f"""
                                <!DOCTYPE html>
                                <html>
                                <body>
                                <table class="table">
                                <thead class="thead-light">
                                <tr>
                                    <th scope="col">First Name</th>
                                    <th scope="col">{member.firstname}</th>
                                </tr>
                                <tr>
                                    <th scope="col">Last Name</th>
                                    <th scope="col">{member.lastname}</th>
                                </tr>
                                </thead>
                                </tbody>
                                </table>
                                    <center><a href="providerMapOn" target="_blank"><button style="background-color: blue;
                                                    color: white;" class="btn btn-outline-success my-2 my-sm-0" type="submit"><strong>Cancel</strong></button></a></center>
                                </body>
                                </html>
                                """, 
                                script=True)
    popup  = folium.Popup(html, max_width=500)
    folium.Marker([pmember.lat, pmember.lng]).add_to(m)
    folium.Marker([member.lat, member.lng],popup=popup,icon = folium.Icon(color='red')).add_to(m)
    folium.PolyLine([(pmember.lat, pmember.lng),(member.lat, member.lng)]).add_to(m)
    m = m._repr_html_() 
    context = {
                    'm' : m,
                    'member': pmember,
                }
    return render(request, 'provider_mapOn.html', context)