# Generated by Django 4.0.5 on 2022-06-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_tag_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(height_field='0', max_length=300, upload_to='images/category/', width_field='0'),
        ),
    ]
