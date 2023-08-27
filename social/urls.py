from django.urls import path
from .views import *

app_name = "social"

urlpatterns = [
    path('', InboxView, name="inbox"),  # by default received msgs will show
    path('received/<str:msg_id>', InboxReceivedView,
         name="inbox_received"),  # received msg data
    path('sent', InboxSentRedirectView,
         name="inbox_sent_redirect"),  # will redirect to the latest sent msg
    path('sent/<str:msg_id>', InboxSentView,
         name="inbox_sent"),  # sent msg data
]
