from django.db import models
from twitteruser.models import TwitterUserModel

class Tweet(models.Model):
    text_content = models.CharField(max_length=280)
    created_time = models.DateTimeField(auto_now_add=True)
    twitter_user = models.ForeignKey(TwitterUserModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.text_content
