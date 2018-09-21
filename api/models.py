from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    event_url = models.URLField(max_length=250)
    img = models.CharField(max_length=255)
    duration = models.IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name
