from django.shortcuts import render
from django.http import HttpResponse
from pomapp.models import Post, PostImage
import json

def home(request):
    return render(request, 'home.html')

def view_post(request, id):
    post = Post.objects.get(id=id)
    next_id = post.id + 1
    prev_id = post.id - 1
    next_post = Post.objects.get(id=next_id)
    previous_post = Post.objects.get(id=prev_id)

    imageObjects = PostImage.objects.filter(post_id = post)
    images = []
    for imageO in imageObjects:
        images.append(imageO.image)

    return render(request, 'post.html', {
        "post": post,
        "image_list": images,
        "next_post": next_post,
        "previous_post": previous_post
    })