from django.contrib import admin

from .models import Event,EventType,SubEventType

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(SubEventType)
