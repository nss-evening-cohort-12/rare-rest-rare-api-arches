from rest_framework import serializers
from rareserverapi.models import RareUsers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUsers
        posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = ('id', 'user', 'bio', 'profile_image_url',
                  'created_on', 'active', 'posts')
        depth = 1
