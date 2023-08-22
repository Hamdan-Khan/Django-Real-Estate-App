from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'gender')
    search_fields = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
