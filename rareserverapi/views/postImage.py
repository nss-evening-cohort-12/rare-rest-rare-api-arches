from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from django.core.files.base import ContentFile
from rareserverapi.models import PostImage
from rest_framework.response import Response
from rest_framework import status
import uuid
import base64


class PostImageViewSet(ViewSet):
    def create(self, request):
        post_image = PostImage()

        fmt, imgstr = request.data["post_image_b64"].split(';base64,')
        ext = fmt.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{uuid.uuid4()}.{ext}')

        post_image.post_image = data

        try:
            post_image.save()
            return Response({"post_image_id": post_image.id}, status=status.HTTP_200_OK)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
