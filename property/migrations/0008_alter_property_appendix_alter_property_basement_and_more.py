# Generated by Django 5.0 on 2024-03-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_remove_property_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='appendix',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='basement',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='elevator',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='furnished',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='kitchen',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='pool',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='roof',
            field=models.BooleanField(default=False, null=True),
        ),
    ]