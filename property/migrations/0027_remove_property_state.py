# Generated by Django 5.0.1 on 2024-06-10 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_alter_property_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='state',
        ),
    ]
