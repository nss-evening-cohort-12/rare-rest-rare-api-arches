from rareserverapi.models.rareUsers import RareUsers
from django.core.exceptions import ValidationError
from django.db.models.fields import NullBooleanField
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareserverapi.models import Subscriptions
from rareserverapi.serializers import SubscriptionsSerializer
from datetime import datetime
from django.db.models import Q


class SubscriptionsViewSet(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            subscription = Subscriptions.objects.get(pk=pk)
            serializer = SubscriptionsSerializer(
                subscription, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        subscriptions = Subscriptions.objects.all()
        follower = request.query_params.get('follower', None)
        author = request.query_params.get('author', None)
        if follower is not None:
            subscriptions = subscriptions.filter(follower_id=follower)
        elif author is not None:
            subscriptions = subscriptions.filter(author_id=author)
        serializer = SubscriptionsSerializer(
          subscriptions, many=True, context={'request': request})
        return Response(serializer.data)

    
    def create(self, request):
        try:
          follower = RareUsers.objects.get(pk=request.data["follower_id"])
          author = RareUsers.objects.get(pk=request.data["author_id"])
          subscription = Subscriptions()
          subscription.follower_id = follower
          subscription.author_id = author
          subscription.ended_on = None

          try:
            exists = Subscriptions.objects.get(follower_id=request.data["follower_id"], author_id=request.data["author_id"])
          except Subscriptions.DoesNotExist as ex:
            try:
              subscription.save()
              serializer = SubscriptionsSerializer(subscription, context={'request': request})
              return Response(serializer.data, status=status.HTTP_201_CREATED)

            except ValidationError as ex:
              return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as ex:
          return HttpResponseServerError(ex)
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
        
          


    def destroy(self, request, pk=None):

        try:
          subscription = Subscriptions.objects.get(pk=pk)
          subscription.delete()

          return Response({}, status=status.HTTP_204_NO_CONTENT)

        except subscription.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        set_end_null = request.data["ended_on"]
        subscription = Subscriptions.objects.get(pk=pk)
        if set_end_null is False:
          subscription.ended_on = None
        else:
          subscription.ended_on = datetime.now()

        subscription.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
