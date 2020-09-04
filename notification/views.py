from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required

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
    notifications = Notification.objects.filter(user_receive=request.user)
    total = 0
    for notif in notifications:
        if notif.notif_flag == False:
            total += 1
    return total