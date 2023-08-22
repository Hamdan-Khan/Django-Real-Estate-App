# Generated by Django 4.2.3 on 2023-08-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_property_size_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='sale_type',
            field=models.CharField(blank=True, choices=[('Sell', 'Sell'), ('Rent', 'Rent')], max_length=10, null=True),
        ),
    ]
