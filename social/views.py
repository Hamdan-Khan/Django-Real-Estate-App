from django.shortcuts import render
from django.db.models import Q
from .models import Message
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
def InboxView(request):
    # retrieves only those msgs in which request.user is present either as sender or receiver
    msgs = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user))

    # makes a list of distinct users with which the request.user has interacted through msgs
    all_users = list(set([i.sender for i in msgs] +
                     [i.receiver for i in msgs]))
    print(all_users)

    profiles = [i.profile for i in all_users]
    # all_users = [ {name:"abc",latest_msg:{text:"ok",date:"Jan"}} , {name:"abc",latest_msg:{text:"ok",date:"Jan"}} ]
    context = {
        'chats': all_users,
        'msgs': msgs,
    }
    return render(request, 'social/inbox.html', context)


@login_required
def InboxDataView(request, msg_id):
    # retrieves only those msgs in which request.user is present either as sender or receiver
    msgs = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user))

    # makes a list of distinct users with which the request.user has interacted through msgs
    all_users = list(set([i.sender for i in msgs] +
                     [i.receiver for i in msgs]))
    print(all_users)

    msg_data = Message.objects.get(id=msg_id)

    context = {
        'chats': all_users,
        'msgs': msgs,
        'msg_data': msg_data
    }
    return render(request, 'social/inbox.html', context)
