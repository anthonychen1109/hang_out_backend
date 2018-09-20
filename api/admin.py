from django.contrib import admin
from .models import User, Location, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Event)
