from rest_framework import serializers
from rareserverapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        post = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ('id', 'post', 'author', 'content', 'subject', 'created_on')
        depth = 2
