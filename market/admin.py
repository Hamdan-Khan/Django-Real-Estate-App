from django.contrib import admin

from .models import *


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'added_at')
    search_fields = ('id', 'title',)


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyType)
admin.site.register(Area)
admin.site.register(City)
