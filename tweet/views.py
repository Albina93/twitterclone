from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . import models
from twitteruser.models import TwitterUserModel
from notification.models import Notification
from . import forms
import re




@login_required
def add_tweet_view(request):
    form = forms.AddTweetForm(request.POST or None)
    if request.POST and form.is_valid():
        data = form.cleaned_data

        new_tweet = models.Tweet.objects.create(
            text_content=data['text_content'],
            twitter_user=request.user
        )
        match_users = re.findall(r'@(\w+)', data.get('text_content'))
        if match_users:
            # users = TwitterUserModel.objects.all()
            for match in match_users:
                new_match = TwitterUserModel.objects.get(username=match)
                if new_match:
                    Notification.objects.create(
                        user_receive=new_match,
                        tweet_receive=new_tweet
                    )
                    
        return HttpResponseRedirect(reverse("homepage"))
                
    form = forms.AddTweetForm()
    return render(request, 'generic.html', {'form': form})
    


def tweet_detail_view(request, tweet_id):
    tweets = models.Tweet.objects.filter(id=tweet_id)
    total_tweets = models.Tweet.objects.filter(twitter_user__username=request.user.username).count()
    return render(request, 'index.html', {'tweets': tweets, 'total_tweets': total_tweets})



