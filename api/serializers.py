from rest_framework import serializers
from .models import (
    User,
    Location,
    Event
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

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
            'description',
            'title',
            'date_time',
            'event_url',
            'img',
            'duration'
        )
