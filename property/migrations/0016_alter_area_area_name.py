# Generated by Django 5.0 on 2024-05-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_alter_property_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_name',
            field=models.CharField(choices=[('الوحدة', 'الوحدة'), ('صنعاء القديمة', 'صنعاء القديمة'), ('شعوب', 'شعوب'), ('أزال', 'أزال'), ('الصافية', 'الصافية'), ('السبعين', 'السبعين'), ('التحرير', 'التحرير'), ('معين', 'معين'), ('الثورة', 'الثورة'), ('بني الحارث', 'بني الحارث')], max_length=100),
        ),
    ]
