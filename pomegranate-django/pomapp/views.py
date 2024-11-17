from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
from pomapp.models import Post, PostImage, NegativePosts
import json
import django.core.serializers as serializers
from django.http import JsonResponse
import os
import pandas as pd
def home(request):
    return render(request, 'home.html')

def view_post(request, id):
    post = Post.objects.get(id=id)
    neg_posts_query = NegativePosts.objects.all()
    neg_post_ids = []
    for obj in neg_posts_query:
        neg_post_ids.append(obj.post_id)
    
    next_id = post.id + 1
    prev_id = post.id - 1
    previous_post_id = -1
    next_post_id = -1
    max_posts = 10

    for i in range(next_id, max_posts+1):
        try:
            next_post = Post.objects.get(id=i)
            next_post_id = next_post.id
        except:
            next_post_id = -1

        if(next_post_id != -1 and next_post_id not in neg_post_ids):
            break;

    for i in range(1, prev_id+1):
        try:
            prev_post = Post.objects.get(id=prev_id)
            previous_post_id = prev_post.id
        except:
            prev_id = prev_id-1
            previous_post_id = -1

        if(previous_post_id != -1 and previous_post_id not in neg_post_ids):
            break;


    imageObject = PostImage.objects.get(post_id = post.id)
    imageString = imageObject.image 
    return render(request, 'post.html', {
        "post": post,
        "image": imageString,
        "next_post_id": next_post_id,
        "previous_post_id": previous_post_id,
    })


def poll_updates(request):
    # Define the path to the CSV file
    csv_path = os.path.join('../pomegranate-brainflow', 'live_data.csv')

    # Check if the file exists
    if not os.path.exists(csv_path):
        return JsonResponse({'error': 'File not found'}, status=404)

    try:
        # Read the CSV file and extract the latest data
        df = pd.read_csv(csv_path, header=None)  # Adjust header=None based on your CSV format
        if df.empty:
            return JsonResponse({'error': 'No data available'}, status=204)
        
        # Extract the latest row
        latest_data = df.iloc[-1].tolist()  # Get the last row as a list
        return JsonResponse({'latest_data': latest_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)