from rest_framework import serializers
from rareserverapi.models import RareUsers
from django.contrib.auth import get_user_model


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUsers
        user = get_user_model()
        posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('id', 'user', 'bio', 'profile_image_url',
                  'created_on', 'active', 'posts')
        depth = 3
