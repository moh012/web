# Generated by Django 5.0 on 2024-04-26 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_property_img_alter_property_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='description',
        ),
    ]