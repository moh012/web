# Generated by Django 5.0 on 2024-05-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_alter_area_area_name_alter_area_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_name',
            field=models.CharField(max_length=100),
        ),
    ]
