from rest_framework import serializers
from rareserverapi.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'rareuser', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
