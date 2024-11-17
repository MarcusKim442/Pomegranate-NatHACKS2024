from contextlib import nullcontext
from django.shortcuts import render
from django.http import HttpResponse
from pomapp.models import Post, PostImage, NegativePosts
import json
import django.core.serializers as serializers
from django.http import JsonResponse
import os
import pandas as pd
import numpy as np
from pomapp.read_eeg import collect_data
from pomapp.extract import gen_training_matrix
from django.conf import settings
import keras
import time

model_path = os.path.join(os.path.dirname(__file__), 'eeg_files', 'custom_model.keras')
eeg_raw_path = os.path.join(os.path.dirname(__file__), 'eeg_files', 'eeg_raw.csv')
eeg_transformed_path = os.path.join(os.path.dirname(__file__), 'eeg_files', 'eeg_transformed.csv')

def home(request):
    return render(request, 'home.html')

def view_post(request, id):
    post = Post.objects.get(id=id)
    neg_posts_query = NegativePosts.objects.all()
    neg_post_ids = []
    for obj in neg_posts_query:
        neg_post_ids.append(obj.post_id)
    
    previous_post_id = -1
    next_post_id = -1
    max_posts = 10

    for i in range(post.id + 1, max_posts+1):
        try:
            next_post = Post.objects.get(id=i)
            next_post_id = next_post.id
        except:
            next_post_id = -1

        if(next_post_id != -1 and next_post_id not in neg_post_ids):
            break;

    for j in range(post.id - 1, 0, -1):
        try:
            prev_post = Post.objects.get(id=j)
            previous_post_id = prev_post.id
        except:
            previous_post_id = -1

        if(previous_post_id != -1 and previous_post_id not in neg_post_ids):
            print(previous_post_id)
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
    
def send_eeg_collection_trigger(request):
    print('see post!')
    collect_data(eeg_raw_path)
    gen_training_matrix(eeg_raw_path, eeg_transformed_path, cols_to_ignore=-1)
    predicted_labels = get_prediction()
    unique_values, counts = np.unique(predicted_labels, return_counts=True)
    most_common = int(unique_values[np.argmax(counts)])
    print("label: ", end='')
    print(most_common)
    return JsonResponse({'data': most_common})

def get_prediction():
    model = keras.saving.load_model(model_path)
    data = pd.read_csv(eeg_transformed_path)
    X_test = data.values 
    X_test = X_test.reshape(data.shape[0], data.shape[1], 1) 
    predictions = model.predict(X_test)
    # For softmax (multiclass classification):
    predicted_labels = predictions.argmax(axis=1)
    print("Predicted labels:", predicted_labels)
    return predicted_labels
