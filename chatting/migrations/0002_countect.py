# Generated by Django 5.0 on 2024-01-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emai', models.EmailField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('details', models.TextField()),
            ],
        ),
    ]