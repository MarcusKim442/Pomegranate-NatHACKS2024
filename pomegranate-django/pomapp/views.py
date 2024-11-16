from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
from pomapp.models import Post, PostImage
import json
import django.core.serializers as serializers
from django.http import JsonResponse
import os
import pandas as pd
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