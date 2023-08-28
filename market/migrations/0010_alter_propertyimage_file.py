# Generated by Django 4.2.3 on 2023-08-28 11:20

from django.db import migrations, models
import market.models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_remove_property_property_pic_propertyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='file',
            field=models.FileField(blank=True, help_text='Allowed size is 50MB', null=True, upload_to=market.models.property_pic_path, validators=[market.models.validate_file_size], verbose_name='Files'),
        ),
    ]
