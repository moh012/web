# Generated by Django 5.0 on 2024-05-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='room_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
