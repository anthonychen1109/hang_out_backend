from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Location, Event

from .serializers import UserProfileSerializer, LocationSerializer, EventSerializer

from .permissions import IsAuthorOrReadOnly

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
