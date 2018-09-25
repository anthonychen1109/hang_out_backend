from rest_framework import serializers
from .models import UserProfile, Category, Group, Event, Tag

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')


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
        )
