from contextlib import nullcontext
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

    try:
        next_post = Post.objects.get(id=next_id)
        next_post_id = next_post.id
    except:
        next_post_id = -1

    try:
        previous_post = Post.objects.get(id=prev_id)
        previous_post_id = previous_post.id
    except:
        previous_post_id = -1


    imageObject = PostImage.objects.get(post_id = post.id)
    imageString = imageObject.image 
    return render(request, 'post.html', {
        "post": post,
        "image": imageString,
        "next_post_id": next_post_id,
        "previous_post_id": previous_post_id,
    })