# Generated by Django 5.0.1 on 2024-06-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0027_remove_property_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
