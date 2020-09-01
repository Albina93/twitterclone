from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . import models
from . import forms



@login_required
def add_tweet_view(request):
    form = forms.AddTweetForm(request.POST or None)
    if request.POST and form.is_valid():
        data = form.cleaned_data
        new_tweet = models.Tweet.objects.create(
            text_content=data['text_content'],
            twitter_user=request.user
        )
        if new_tweet:
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    return render(request, 'generic.html', {'form': form})
    

