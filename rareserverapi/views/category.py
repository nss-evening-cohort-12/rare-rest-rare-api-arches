from django.http.response import HttpResponseServerError
from rareserverapi.serializers.category import CategorySerializer
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareserverapi.models import Category, RareUsers
from rareserverapi.serializers import CategorySerializer

class CategoriesViewSet(ViewSet):


    def create(self, request):

        creator = RareUsers.objects.get(user=request.auth.user)

        category = Category()
        category.label = request.data["label"]
        category.approved = True
        category.rareuser = creator

        try:
            category.save()
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):

        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)
