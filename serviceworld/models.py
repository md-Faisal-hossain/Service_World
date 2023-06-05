from django.db import models

# Create your models here.

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=25)
    lat=models.FloatField()
    lng=models.FloatField()
    image = models.ImageField(upload_to='images')  

    def __str__(self):
        return self.firstname + " " + self.lastname
    

class ProviderMember(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=25)
    category=models.CharField(max_length=30)
    experience=models.CharField(max_length=12)
    phone=models.CharField(max_length=25)
    lat=models.FloatField()
    lng=models.FloatField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.firstname + " " + self.lastname
    

class ConnectionRequest(models.Model):
    mid = models.IntegerField()
    pid = models.IntegerField()

