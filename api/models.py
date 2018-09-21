from django.db import models
# djangos user is stored here
from django.contrib.auth.models import User
# allows you to execute code with actions happening in the DB
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    # set up link to djangos User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    bio = models.TextField()

    def __str__(self):
        return self.name

# create user profile when we create the default django User
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    # events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def de_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    event_url = models.URLField(max_length=250, default='')
    img = models.URLField(max_length=255, default='')
    duration = models.IntegerField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
