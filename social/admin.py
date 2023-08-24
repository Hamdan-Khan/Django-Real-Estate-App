from django.contrib import admin

from .models import *


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'sent_at')
    search_fields = ('id', 'sender',)


admin.site.register(Message, MessageAdmin)
