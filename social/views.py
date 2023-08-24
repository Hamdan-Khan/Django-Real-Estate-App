from django.shortcuts import render


def InboxView(request):
    return render(request, 'social/inbox.html')
