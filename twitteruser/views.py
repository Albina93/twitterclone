from django.shortcuts import render, HttpResponseRedirect
from .models import TwitterUserModel
from tweet.models import Tweet
# from django.contrib.auth.decorators import login_required
from notification import views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required(login_url="loginpage")
# def index_view(request):
#     total_tweets = Tweet.objects.filter(twitter_user__username=request.user.username).count()
    
#     user_tweets = Tweet.objects.filter(twitter_user=request.user).order_by('-created_time') 
#     following_tweets = Tweet.objects.filter(twitter_user__in=request.user.following.all()).order_by('-created_time') 
#     tweets = user_tweets | following_tweets
#     notif_count = views.total_count(request)

#     return render(request, 'index.html', {'tweets': tweets, 'total_tweets': total_tweets, 'notif_count': notif_count})


class IndexView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        total_tweets = Tweet.objects.filter(twitter_user__username=request.user.username).count()
        user_tweets = Tweet.objects.filter(twitter_user=request.user).order_by('-created_time') 
        following_tweets = Tweet.objects.filter(twitter_user__in=request.user.following.all()).order_by('-created_time') 
        tweets = user_tweets | following_tweets
        notif_count = views.total_count(request)
        return render(request, 'index.html', {'tweets': tweets, 'total_tweets': total_tweets, 'notif_count': notif_count})




# def profile_view(request, user_name):
#     user_profile = TwitterUserModel.objects.get(username=user_name)
#     tweets = Tweet.objects.filter(twitter_user__username=user_name).order_by('-created_time')
#     total_tweets = tweets.count()
#     if request.user.is_authenticated:
#         following_list = request.user.following.all()
#     else:
#         following_list = []

#     return render(request, 'profile.html', {'tweets': tweets, 'total_tweets': total_tweets,  'user_profile': user_profile, 'following_list': following_list})


class ProfileView(TemplateView):
    def get(self, request, user_name):
        user_profile = TwitterUserModel.objects.get(username=user_name)
        tweets = Tweet.objects.filter(twitter_user__username=user_name).order_by('-created_time')
        total_tweets = tweets.count()
        if request.user.is_authenticated:
            following_list = request.user.following.all()
        else:
            following_list = []

        return render(request, 'profile.html', {'tweets': tweets, 'total_tweets': total_tweets,  'user_profile': user_profile, 'following_list': following_list})


    

# def add_follow_view(request, user_name):
#     user_follow = TwitterUserModel.objects.get(username=user_name)
#     login_user = TwitterUserModel.objects.get(username=request.user.username)
#     login_user.following.add(user_follow)
#     login_user.save()


#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


class AddFollowView(TemplateView):
    def get(self, request, user_name):
        user_follow = TwitterUserModel.objects.get(username=user_name)
        login_user = TwitterUserModel.objects.get(username=request.user.username)
        login_user.following.add(user_follow)
        login_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


# def add_unfollow_view(request, user_name):
#     user_unfollow = TwitterUserModel.objects.get(username=user_name)
#     login_user = TwitterUserModel.objects.get(username=request.user.username)
#     login_user.following.remove(user_unfollow)

#     login_user.save()

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


class AddUnfollowView(TemplateView):
    def get(self, request, user_name):
        user_unfollow = TwitterUserModel.objects.get(username=user_name)
        login_user = TwitterUserModel.objects.get(username=request.user.username)
        login_user.following.remove(user_unfollow)

        login_user.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
