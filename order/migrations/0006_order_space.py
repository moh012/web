# Generated by Django 5.0 on 2023-12-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_order_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='space',
            field=models.IntegerField(null=True),
        ),
    ]
