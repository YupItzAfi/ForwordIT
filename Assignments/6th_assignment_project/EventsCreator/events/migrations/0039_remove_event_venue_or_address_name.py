# Generated by Django 4.1.1 on 2022-10-28 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_event_venue_or_address_name_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='venue_or_address_name',
        ),
    ]
