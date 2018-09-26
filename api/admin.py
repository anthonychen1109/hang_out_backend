from django.contrib import admin
from .models import Event, Category, Tag, Group

# Register your models here.
# admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Group)
