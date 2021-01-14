from rest_framework import serializers
from rareserverapi.models import Subscriptions

class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        follower_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        author_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
        fields = ('id', 'follower_id', 'author_id', 'created_on', 'ended_on')
