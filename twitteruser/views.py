from django.shortcuts import render, HttpResponseRedirect
from .models import TwitterUserModel
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required(login_url="loginpage")
def index_view(request):
    tweets = Tweet.objects.all().order_by('-created_time')
    total_tweets = Tweet.objects.filter(twitter_user__username=request.user.username).count()
    return render(request, 'index.html', {'tweets': tweets, 'total_tweets': total_tweets})



def profile_view(request, user_name):
    tweets = Tweet.objects.filter(twitter_user__username=user_name).order_by('-created_time')
    total_tweets = tweets.count()
    return render(request, 'index.html', {'tweets': tweets, 'total_tweets': total_tweets})


def add_follow_view(request, user_name):
    user_follow = TwitterUserModel.objects.get(username=user_name)
    login_user = TwitterUserModel.objects.get(username=request.user.username)
    login_user.following.add(user_follow)
    

    login_user.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def add_unfollow_view(request, user_name):
    user_unfollow = TwitterUserModel.objects.get(username=user_name)
    login_user = TwitterUserModel.objects.get(username=request.user.username)
    login_user.following.remove(user_unfollow)

    login_user.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
