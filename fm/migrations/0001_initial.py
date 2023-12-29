# Generated by Django 5.0 on 2023-12-29 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial_Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField()),
                ('method', models.CharField(max_length=100)),
                ('data_time', models.DateTimeField()),
                ('reference', models.CharField(max_length=100)),
                ('admin_configration', models.BooleanField()),
                ('im_port', models.DecimalField(decimal_places=2, max_digits=5)),
                ('export', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.ImageField(upload_to='')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.agent')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(max_length=50)),
                ('notification_text', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
