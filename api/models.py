from django.db import models
# djangos user is stored here
from django.contrib.auth.models import User
# allows you to execute code with actions happening in the DB
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    # set up link to djangos User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user

# create user profile when we create the default django User
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    event_url = models.URLField(max_length=250, default='')
    img = models.URLField(max_length=255, default='')
    duration = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

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

class Friend(models.Model):
    users = models.ManyToManyField(User)
