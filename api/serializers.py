from rest_framework import serializers
from .models import UserProfile, Category, Group, Event, Tag

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name','bio')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class TagSerializer(models.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class GroupSerializer(models.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'admin_id',
            'name',
            'category_id',
            'description',
            'users',
            'tags'
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'address',
            'country',
            'city',
            'date',
            'users'
        )
