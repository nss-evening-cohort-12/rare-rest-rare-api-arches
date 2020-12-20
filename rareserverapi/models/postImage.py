from django.db import models


class PostImage(models.Model):
    post_image = models.ImageField(
        upload_to='post_images', height_field=None,
        width_field=None, max_length=None, null=True
    )
