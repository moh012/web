# Generated by Django 5.0 on 2024-05-11 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_agent_state_customer_state'),
        ('order', '0012_alter_order_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='accounts.customer'),
        ),
    ]
