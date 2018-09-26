from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

from .models import (
    # User,
    Category,
    Group,
    Event,
    Tag
)

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class GroupSerializer(serializers.ModelSerializer):
    num_users = serializers.SerializerMethodField()
    # adds methods to serializers
    # tags = serializers.StringRelatedField(many=True)
    # category = serializers.StringRelatedField()
    # admin_id = serializers.StringRelatedField()
    # serializer relationships and represent them as strings
    # users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = (
            'id',
            'group_creator',
            'name',
            'category',
            'description',
            'users',
            # 'tags',
            'num_users',
        )

    def get_num_users(self, obj):
        return obj.num_users()

class CategorySerializer(serializers.ModelSerializer):
    groups = GroupSerializer(source='cat_group', many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'cat_img', 'groups')
        # depth = 1

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'address',
            'country',
            'city',
            'date',
            'users',
            'group_id',
            'event_img',
        )
