# Generated by Django 5.0.1 on 2024-06-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_agent_address_agent_facebook_agent_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='slug',
        ),
        migrations.AddField(
            model_name='customer',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
