# Generated by Django 5.0.1 on 2024-06-04 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fm', '0009_financial_movement_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial_movement',
            name='created_by',
        ),
    ]
