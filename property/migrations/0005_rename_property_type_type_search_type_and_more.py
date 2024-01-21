# Generated by Django 5.0 on 2024-01-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_rename_tescription_property_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='property_type',
            new_name='search_type',
        ),
        migrations.RemoveField(
            model_name='type',
            name='type_name',
        ),
        migrations.AddField(
            model_name='property',
            name='appendix',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='basement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='build_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='elevator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='floor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='furnished',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='hall_room',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='pool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='room_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='space',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='street_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='type_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='features',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
