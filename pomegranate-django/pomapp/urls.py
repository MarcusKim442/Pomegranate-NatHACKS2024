from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>', views.view_post, name='view_post'),
    path('poll_updates', views.poll_updates, name='poll_updates'),
]