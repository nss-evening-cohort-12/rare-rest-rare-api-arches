from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareserverapi.models import Category
from rareserverapi.serializers import CategorySerializer


class CategoriesViewSet(ViewSet):

    def retrieve(self, request, pk=None):

        try:
          category = Category.objects.get(pk=pk)
          serializer = CategorySerializer(category, context={'request': request})
          return Response(serializer.data)
        except Exception as ex:
          return HttpResponseServerError(ex)

    def list(self, request):

      categories = Category.objects.all().order_by('label')

      serializer = CategorySerializer(
        categories, many=True, context={'request': request})
      return Response(serializer.data)
