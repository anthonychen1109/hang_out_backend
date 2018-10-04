from django.db import models
# djangos user is stored here
from django.contrib.auth.models import User
# allows you to execute code with actions happening in the DB
from django.db.models.signals import post_save
from datetime import datetime

# Create your models here.
# class UserProfile(User):
#     # set up link to djangos User model
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, default='')
#     email = models.EmailField(default='')
#
#     def __str__(self):
#         return self.name

# create user profile when we create the default django User
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender = User)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cat_img = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    hometown = models.CharField(max_length=255, default='')
    group_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizer_name", default=1)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='cat_group', on_delete=models.CASCADE)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='group_users', default=1)
    group_img = models.TextField(default="")
    # tags = models.ManyToManyField(Tag, related_name='tags')

    def user_names(self):
        user_names = self.users.all()
        data = [str(usr) for usr in user_names]
        return data

    def num_users(self):
        return self.users.all().count()

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=20, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    users = models.ManyToManyField(User, related_name='event_users')
    group_id = models.ForeignKey(Group, related_name="group_events", on_delete=models.CASCADE)
    event_img = models.TextField(default='')
    details = models.TextField(default='')
    # events = models.ManyToManyField(Event)

    def organizer(self):
        user_names = self.users.all()
        data = [str(usr) for usr in user_names]
        return data[0]

    def __str__(self):
        return self.name

class Friend(models.Model):
    users = models.ManyToManyField(User, related_name='friend_users')
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
