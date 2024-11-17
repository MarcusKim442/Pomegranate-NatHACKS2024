from datetime import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    profile_photo = models.CharField(max_length=4000, blank=False)
    user = models.CharField(max_length = 20)
    title = models.CharField(max_length=100, blank=False)
    caption = models.CharField(max_length=500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


class PostImage(models.Model):
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    image = models.CharField(max_length=1000, blank=False)

class NegativePosts(models.Model):
    post_id = models.IntegerField()
