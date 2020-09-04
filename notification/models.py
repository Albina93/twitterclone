from django.db import models
from twitteruser.models import TwitterUserModel
from tweet.models import Tweet

class Notification(models.Model):
    user_receive = models.ForeignKey(TwitterUserModel, on_delete=models.CASCADE, related_name="receive")
    tweet_receive = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_receive")
    notif_flag = models.BooleanField(default=False)

    
   

