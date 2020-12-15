from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareserverapi.models import Post, Tag

class PostTagViewSet(ViewSet):

    def create(self, request):
        post = Post.objects.get(pk=request.data["post_id"])
        taglist = request.data["tags"]

        for tagId in taglist:
          singleTag = Tag.objects.get(pk=tagId)
          post.tags.add(singleTag)          
        
        return Response({"message": "tags added to post"}, status=status.HTTP_200_OK)
    
    def destroy(self, post, tag):
        post_id = self.kwargs['post']
        tag_id = self.kwargs['tag']

        try:
            post = Post.objects.get(pk=post_id)
            tag = Tag.objects.get(pk=tag_id)
            post.tag.delete(tag)

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
