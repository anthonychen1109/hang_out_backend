from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
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
    authentication_classes = [TokenAuthentication,]

class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny,]
