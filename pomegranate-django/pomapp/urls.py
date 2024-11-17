from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pomapp/post/<int:id>', views.view_post, name='view_post'),
    path('poll', views.poll_updates, name='poll'),

]