from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    event_url = models.URLField(max_length=250)
    img = models.CharField(max_length=255)
    duration = models.IntegerField()
    users = models.ManyToManyField(User)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    events = models.ManyToManyField(Event)
