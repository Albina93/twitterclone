from django.urls import path
from . import views

urlpatterns = [
    path('add_tweet/', views.add_tweet_view, name="addtweet"),
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name="tweet_details"),
    
   
]