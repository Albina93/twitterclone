from django.shortcuts import render

def notification_view(request):
    return render(request, 'index.html',)

