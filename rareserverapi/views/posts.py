from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareserverapi.models import Post, RareUsers, Category, Tag, PostReactions
from rareserverapi.serializers import PostSerializer
from rest_framework.decorators import action


class PostsViewSet(ViewSet):

    def create(self, request):
        creator = RareUsers.objects.get(user=request.auth.user)

        post = Post()
        post.title = request.data["title"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.approved = creator.user.is_staff
        post.rareuser = creator

        category = Category.objects.get(pk=request.data["category_id"])
        post.category = category

        try:
            post.save()
            post.tags.set(request.data["tags"])
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.approved = True

        category = Category.objects.get(pk=request.data["category_id"])
        post.category = category
        post.tags.set(request.data["tags"])
        post.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            # If user is an admin (is_staff == true), then we can just
            # delete the post by pk.  Otherwise, we should verify that
            # the user owns that post before deleting it.
            if request.user.is_staff:
                post = Post.objects.get(pk=pk)
            else:
                post = Post.objects.get(pk=pk, rareuser_id=request.user.id)

            post.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        posts = Post.objects.all()
        category = self.request.query_params.get('category', None)
        user = self.request.query_params.get('user', None)

        # These filters all you to do http://localhost:8000/posts?category=1 or
        # http://localhost:8000/posts?user=1 or
        # http://localhost:8000/posts?category=1&user=2

        if category is not None:
            posts = posts.filter(category__id=category)

        if user is not None:
            posts = posts.filter(rareuser__id=user)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def remove_tag(self, request, pk=None):

        try:
            post = Post.objects.get(pk=pk)
            tag = Tag.objects.get(pk=request.data['tag_id'])
            post.tags.remove(tag)

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
