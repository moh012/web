# Generated by Django 5.0 on 2024-02-05 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_agent_photo_customer_photo'),
        ('chatting', '0011_remove_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer'),
        ),
    ]