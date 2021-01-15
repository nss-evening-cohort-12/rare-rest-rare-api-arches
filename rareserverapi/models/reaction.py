from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Reaction(models.Model):
    label = models.CharField(max_length=25)
    image_url = models.CharField(max_length=500)


class PostReactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    reaction = models.ForeignKey("Reaction", on_delete=CASCADE)

    class Meta:
        unique_together = ('user', 'reaction',)
