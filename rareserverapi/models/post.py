from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

class Post(models.Model):
    rareuser = models.ForeignKey(
        "RareUsers", 
        on_delete=CASCADE, 
        related_name="posts", 
        related_query_name="post"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=SET_NULL, 
        related_name="posts", #did not add CASCADE here, so post stays even after category is deleted
        related_query_name= "post",
        null=True, #added here if the category was deleted
        blank=True
    )
    title = models.CharField(max_length=75)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.CharField(max_length=255)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        "Tag",
        related_name="tag_posts",
        related_query_name="tag_post"
    )
