# Generated by Django 4.0.5 on 2022-06-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
