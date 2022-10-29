# Generated by Django 4.1.1 on 2022-09-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('In-person', 'In-person'), ('Streaming', 'Streaming'), ('In-person and Streaming', 'In-person and Streaming')], max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='stream',
            field=models.CharField(choices=[('Secured_Promotix', 'Secured Promotix'), ('Unsecured-Other', 'Unsecured - Other')], max_length=20),
        ),
    ]
