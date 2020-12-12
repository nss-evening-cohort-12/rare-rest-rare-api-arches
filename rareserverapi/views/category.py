from rest_framework.viewsets import ViewSet
from rareserverapi.models import Category
from rareserverapi.serializers import CategorySerializer
from django.http import HttpResponseServerError
from rest_framework.response import Response

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
