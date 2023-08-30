from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Message
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
def InboxView(request):
    # retrieves only those msgs in which request.user is present either as sender or receiver
    # msgs = Message.objects.filter(
    #     Q(sender=request.user) | Q(receiver=request.user))
    msgs = Message.objects.filter(receiver=request.user).order_by("-sent_at")

    # makes a list of distinct users with which the request.user has interacted through msgs
    # all_users = list(set([i.sender for i in msgs] +
    #                  [i.receiver for i in msgs]))
    all_users = [i.sender for i in msgs]

    print(all_users)

    context = {
        'chats': all_users,
        'msgs': msgs,
    }
    return render(request, 'social/inbox.html', context)


@login_required
def InboxReceivedView(request, msg_id):
    # retrieves only those msgs in which request.user is present as receiver
    msgs = Message.objects.filter(receiver=request.user).order_by("-sent_at")

    # makes a list of users that sent request.user msgs
    all_users = [i.sender for i in msgs]

    msg_data = msgs.get(id=msg_id)

    context = {
        'chats': all_users,
        'msgs': msgs,
        'msg_data': msg_data
    }
    return render(request, 'social/inbox.html', context)


@login_required
def InboxSentRedirectView(request):
    # retrieves only those msgs in which request.user is present as sender
    msgs = Message.objects.filter(sender=request.user).order_by("-sent_at")

    if msgs.count() > 0:
        msg_id = msgs[0].id

        return redirect('social:inbox_sent', msg_id)
    else:
        context = {
            'is_sent': True,
            'none_sent': True,
            'none_sent_text': "Oops! It seems you have not sent any messages. You can visit the properties listed on our site and inquire owners about the property."
        }
        return render(request, 'social/inbox.html', context)


@login_required
def InboxSentView(request, msg_id):
    # retrieves only those msgs in which request.user is present as sender
    msgs = Message.objects.filter(sender=request.user).order_by("-sent_at")

    # makes a list of users that received msgs from request.user
    all_users = [i.receiver for i in msgs]

    print(all_users)

    msg_data = msgs.get(id=msg_id)

    context = {
        'chats': all_users,
        'msgs': msgs,
        'msg_data': msg_data,
        'is_sent': True
    }
    return render(request, 'social/inbox.html', context)
