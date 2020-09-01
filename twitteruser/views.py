from django.shortcuts import render
from .models import TwitterUserModel
from tweet.models import Tweet

def index_view(request):
    all_tweets = Tweet.objects.all()
    return render(request, 'index.html', {'all_tweets': all_tweets})
