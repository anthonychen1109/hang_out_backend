from django.contrib import admin
from .models import UserProfile, Location, Event

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Event)
