from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('fetch-tweets/', fetchtweets, name='fetchtweets'),
    path('add-tweets/', addtweets, name='addtweet'),
    path('fetch-tweets-filter/', fetchtweetsfilter, name='fetchtweetsfilter'),
    
]

# v-on:submit.prevent="submitForm"