from django.contrib import admin
from events.models import Event


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "event_date", "_participants"]

    def _participants(self, event):
        return event.participants.count()

