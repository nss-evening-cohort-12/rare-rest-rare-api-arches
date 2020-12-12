from rest_framework import serializers
from rareserverapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        author_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        post_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ('id', 'post_id', 'author_id', 'content', 'subject', 'created_on')
        depth = 1
