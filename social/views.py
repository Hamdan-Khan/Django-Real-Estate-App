from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required


# basic landing view of inbox page with list of received msgs
@login_required
def InboxView(request):
    # retrieves only those msgs in which request.user is present as receiver
    msgs = Message.objects.filter(receiver=request.user).order_by("-sent_at")

    context = {
        'msgs': msgs,
    }
    return render(request, 'social/inbox.html', context)


# detailed view of received msg
@login_required
def InboxReceivedView(request, msg_id):
    # retrieves only those msgs in which request.user is present as receiver
    msgs = Message.objects.filter(receiver=request.user).order_by("-sent_at")

    msg_data = msgs.get(id=msg_id)

    context = {
        'msgs': msgs,
        'msg_data': msg_data
    }
    return render(request, 'social/inbox.html', context)


# view of sent msgs which redirects to the latest sent msg detail if present, else it will display a text msg.
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

# view redirected from the sent msgs page, shows detail of sent msg


@login_required
def InboxSentView(request, msg_id):
    # retrieves only those msgs in which request.user is present as sender
    msgs = Message.objects.filter(sender=request.user).order_by("-sent_at")

    # makes a list of users that received msgs from request.user
    all_users = [i.receiver for i in msgs]

    msg_data = msgs.get(id=msg_id)

    context = {
        'chats': all_users,
        'msgs': msgs,
        'msg_data': msg_data,
        'is_sent': True
    }
    return render(request, 'social/inbox.html', context)
