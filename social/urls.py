from django.urls import path
from .views import *

app_name = "social"

urlpatterns = [
    path('', InboxView, name="inbox"),
    path('<str:msg_id>', InboxDataView, name="inbox_data"),
]
