# Generated by Django 4.2.3 on 2023-09-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_propertyimage_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='province',
            field=models.CharField(blank=True, choices=[('Sindh', 'Sindh'), ('Punjab', 'Punjab'), ('Balochistan', 'Balochistan'), ('KPK', 'KPK')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='name',
            field=models.CharField(choices=[('Plot', 'Plot'), ('Shop', 'Shop'), ('House', 'House')], max_length=40),
        ),
    ]
