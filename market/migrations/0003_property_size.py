# Generated by Django 4.2.3 on 2023-08-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_area_city_remove_property_name_property_added_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
