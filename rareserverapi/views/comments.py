from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareserverapi.models import Post, RareUsers, Comment
from rareserverapi.serializers import CommentSerializer

class CommentViewSet(ViewSet):

    def create(self, request):
        creator = RareUsers.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["post_id"])

        comment = Comment()
        comment.post_id = post
        comment.content = request.data["content"]
        comment.subject = request.data["subject"]
        comment.author_id = creator

        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        creator = RareUsers.objects.get(user=request.auth.user)

        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        comment.subject = request.data["subject"]

        comment.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        comments = Comment.objects.all()
        post = self.request.query_params.get('post', None)
        user = self.request.query_params.get('user', None)

        # These filters allow you to do http://localhost:8000/comments?post=1 or
        # http://localhost:8000/comments?user=1 or
        # http://localhost:8000/comments?user=1&post=2
        
        if  post is not None:
            comments = comments.filter(post_id_id=post)

        if user is not None:
            comments = comments.filter(author_id_id=user)

        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)
