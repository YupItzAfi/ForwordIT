# Generated by Django 4.1.1 on 2022-10-28 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0035_auto_20221028_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_ticket_type',
            name='type',
            field=models.CharField(choices=[('ga_ticket', 'GA Ticket'), ('vip_ticket', 'VIP Ticket'), ('reserved_seating', 'Reserved Seating'), ('members_only_ticket', 'Members-only Ticket'), ('giveaway_ticket', 'Giveaway Ticket'), ('group_package_ticket', 'Group Package Ticket')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='refund',
            name='reason',
            field=models.CharField(choices=[('1', 'Duplicate'), ('2', 'Fraudulent'), ('3', 'Requested by Customer'), ('4', 'Expired uncaptured charge')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ticket_booking',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_event_id', to='events.event'),
        ),
        migrations.AlterField(
            model_name='ticket_booking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]