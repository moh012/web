# Generated by Django 5.0 on 2024-01-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial_movement',
            name='img',
            field=models.ImageField(upload_to='fmPhoto/%Y/%m/%d/'),
        ),
    ]
