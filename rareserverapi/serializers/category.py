from rest_framework import serializers
from rareserverapi.models import category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = ('id', 'label')
