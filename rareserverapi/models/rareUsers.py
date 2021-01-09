from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class RareUsers(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
  bio = models.TextField()
  profile_image_url = models.CharField(max_length=255)
  created_on = models.DateField(auto_now_add=True)
