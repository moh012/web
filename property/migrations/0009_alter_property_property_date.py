# Generated by Django 5.0 on 2024-03-02 01:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_property_appendix_alter_property_basement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
