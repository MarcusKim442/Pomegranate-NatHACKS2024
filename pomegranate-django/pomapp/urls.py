from django.urls import path
from . import views

urlpatterns = [
    path('pomapp', views.home, name='home'),
    path('pomapp/post/<int:id>', views.view_post, name='view_post'),
    path('poll', views.poll_updates, name='poll'),
    path('begin-collection', views.send_eeg_collection_trigger, name='begin-collection'),
]