from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    User,
    Location,
    Event
)
from .serializers import (
    UserSerializer,
    LocationSerializer,
    EventSerializer
)

from .permissions import IsAuthorOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
