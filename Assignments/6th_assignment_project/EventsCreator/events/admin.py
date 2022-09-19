from django.contrib import admin
from .models import *

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'event_type', 'stream',
                    'venue_or_address_name', 'time', 'person_ticket_name', 'quantity', 'price', ]

    list_filter = ['user', 'category', 'event_type', 'stream',
                   'venue_or_address_name', 'time', 'person_ticket_name', 'quantity', 'price', ]


admin.site.register(Event, EventAdmin)
admin.site.register(Refund)
admin.site.register(Ticket_Booking)
admin.site.register(Time_Schedule)
admin.site.register(Create_Ticket_Type)
admin.site.register(Volunteer_Ticket)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Categorie)
admin.site.register(Currencie)
admin.site.register(Venue)
