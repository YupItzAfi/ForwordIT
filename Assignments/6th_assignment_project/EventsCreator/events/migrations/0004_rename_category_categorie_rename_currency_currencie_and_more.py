# Generated by Django 4.1.1 on 2022-09-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_payments_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Currency',
            new_name='Currencie',
        ),
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]