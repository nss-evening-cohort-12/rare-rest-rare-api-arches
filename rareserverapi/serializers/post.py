from rest_framework import serializers
from rareserverapi.models import Post, PostReactions


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        rareuser = serializers.PrimaryKeyRelatedField(
            many=False, read_only=True)
        category = serializers.PrimaryKeyRelatedField(
            many=False, read_only=True)
        fields = ('id', 'rareuser', 'category', 'title',
                  'publication_date', 'image_url', 'content', 'approved', 'tags',
                  'reactions')
        depth = 2
