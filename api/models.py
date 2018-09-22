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

    def __str__(self):
        return self.name

# create user profile when we create the default django User
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    users = models.ManyToManyField(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date = models.DateTimeField()
    users = models.ManyToManyField(User)
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
