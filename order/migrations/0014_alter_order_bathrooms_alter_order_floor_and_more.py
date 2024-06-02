# Generated by Django 5.0 on 2024-06-01 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bathrooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='floor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='hall_room',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='housetype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='room_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
