from django.contrib import admin
from pomapp.models import PostImage, Post, NegativePosts

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(NegativePosts)
