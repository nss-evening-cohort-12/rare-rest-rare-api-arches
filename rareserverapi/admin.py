from django.contrib import admin
from rareserverapi.models import Post,Tag,Category,RareUsers
# Register your models here.
admin.site.register(RareUsers)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)