# Generated by Django 4.1.1 on 2022-09-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_currencie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencie',
            name='name',
            field=models.CharField(choices=[('usd', 'Dollars'), ('bdt', 'Taka'), ('aed', 'UAE Dirham'), ('kwd', 'Kuwait Dinar'), ('jpy', 'Japanian Yen')], max_length=50),
        ),
    ]