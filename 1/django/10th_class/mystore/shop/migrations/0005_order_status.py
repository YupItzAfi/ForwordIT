# Generated by Django 4.0.5 on 2022-06-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out of Delivery', 'Out of Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]