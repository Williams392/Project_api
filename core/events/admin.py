from django.contrib import admin
from .models import *

class VisibilityOptionsAdmin(admin.ModelAdmin):
    list_display = ('name', )

class StatusOptionsAdmin(admin.ModelAdmin):
    list_display = ('name', )

class EventTypeOptionsAdmin(admin.ModelAdmin):
    list_display = ('name', )

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'hour', 'location', 'e_type')
    list_filter = ('date', 'e_type')
    search_fields = ('title', 'location')

class PresentsAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_event')

class InterestedAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_event')

class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'price')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_type', 'assigned_to', 'code')

admin.site.register(VisibiltyOptions, VisibilityOptionsAdmin)
admin.site.register(StatusOptions, StatusOptionsAdmin)
admin.site.register(EventTypeOptions, EventTypeOptionsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Presents, PresentsAdmin)
admin.site.register(Interested, InterestedAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Ticket, TicketAdmin)
