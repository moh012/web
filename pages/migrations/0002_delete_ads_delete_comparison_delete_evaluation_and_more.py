# Generated by Django 5.0 on 2023-12-23 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ADS',
        ),
        migrations.DeleteModel(
            name='Comparison',
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Financial_Movement',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Photo_ADS',
        ),
        migrations.DeleteModel(
            name='Photo_Property',
        ),
        migrations.DeleteModel(
            name='Report_Customer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]