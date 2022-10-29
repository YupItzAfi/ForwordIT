# Generated by Django 4.1.1 on 2022-10-28 11:54

from django.db import migrations
from django.apps import apps

import events.models


def link(schema_editor, apps=apps):
    Event = events.models.Event
    Venue = events.models.Venue
    for event in Event.objects.all():
        venue, location = Venue.objects.get_or_create(
            name=event.venue_or_address_name)
        event.venue_or_address_name_link = location
        event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_event_venue_or_address_name_link_and_more'),
    ]

    operations = [
        migrations.RunPython(link)
    ]
