from rest_framework import serializers
from rareserverapi.models import PostReactions


class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReactions
        fields = ('id', 'reaction_id', 'user_id')
