# Generated by Django 5.0 on 2024-01-17 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0003_rename_countect_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emai',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='details',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='title',
            new_name='subject',
        ),
    ]
