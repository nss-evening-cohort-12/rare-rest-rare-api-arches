# from django.core.exceptions import ValidationError
# from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rareserverapi.models import RareUsers
from rareserverapi.serializers import UsersSerializer
# from rest_framework import serializers
# from rest_framework import status
# from rareserverapi.models import Post, RareUsers, Category, Tag
# from rest_framework.decorators import action


class UsersViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            user = RareUsers.objects.get(pk=pk)
            serializer = UsersSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
