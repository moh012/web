# Generated by Django 5.0 on 2024-02-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
