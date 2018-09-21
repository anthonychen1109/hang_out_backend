from django.shortcuts import render
from rest_framework import viewsets
from .models import Location, Event

from .serializers import LocationSerializer, EventSerializer

from .permissions import IsAuthorOrReadOnly

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
