from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, Event, Category, Tag, Group

from .serializers import (
    UserProfileSerializer,
    EventSerializer,
    CategorySerializer,
    TagSerializer,
    GroupSerializer
)

from .permissions import IsAuthorOrReadOnly

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.obects.all()
    serializer_class = TagSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
