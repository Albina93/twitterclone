from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url="loginpage")
def notification_view(request):
    notifications = Notification.objects.filter(user_receive=request.user)
    
    new_notif = []
    for notif in notifications:
        if notif.notif_flag == False:
            
            new_notif.append(notif.tweet_receive)
            notif.notif_flag = True
            notif.save()

    return render(request, "notification.html", {'new_notif': new_notif})



def total_count(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user_receive=request.user)
        total = 0
        for notif in notifications:
            if notif.notif_flag == False:
                total += 1
    else:
        total = 0
    return total