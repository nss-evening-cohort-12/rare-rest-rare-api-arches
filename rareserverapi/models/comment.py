from django.db import models
from django.db.models.deletion import CASCADE

class Comment(models.Model):
    post_id = models.ForeignKey(
        "Post",
        on_delete=CASCADE, 
        related_name="posts",
        related_query_name= "post",
        null=False,
        blank=True
    )
    author_id = models.ForeignKey(
        "RareUsers", 
        on_delete=CASCADE, 
        related_name="rareusers", 
        related_query_name="rareuser"
    )
    content = models.TextField()
    subject = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
