from rest_framework import serializers
from .models import UserProfile, Location, Event

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name','bio')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'address',
            'lat',
            'lng',
            'country',
            'city'
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'user',
            'description',
            'title',
            'date_time',
            'event_url',
            'img',
            'duration'
        )
