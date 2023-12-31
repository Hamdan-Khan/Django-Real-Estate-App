# models
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# storage
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def property_pic_path(instance, filename):
    return os.path.join('property_pics', filename)


class PropertyType(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ("Plot", "Plot"),
        ("Shop", "Shop"),
        ("House", "House"),
    ]
    name = models.CharField(choices=PROPERTY_TYPE_CHOICES, max_length=40)

    def __str__(self):
        return self.name


# malir/gulshan etc
class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Property(models.Model):
    UNIT_CHOICES = [
        ("Square feet", "sq.ft"),
        ("Square meters", "sq.m"),
        ("Marla", "marla"),
        ("Kanal", "kanal"),
    ]
    SALE_CHOICES = [
        ("Sell", "Sell"),
        ("Rent", "Rent"),
    ]
    PROVINCE_CHOICES = [
        ("Sindh", "Sindh"),
        ("Punjab", "Punjab"),
        ("Balochistan", "Balochistan"),
        ("KPK", "KPK"),
    ]
    title = models.CharField(max_length=300, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey(
        PropertyType, on_delete=models.CASCADE, related_name="property", blank=True, null=True)
    sale_type = models.CharField(
        max_length=10, choices=SALE_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    size_unit = models.CharField(
        choices=UNIT_CHOICES, blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    province = models.CharField(
        choices=PROVINCE_CHOICES, max_length=40, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="property_city", null=True, blank=True)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="area", null=True, blank=True)
    added_at = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else str(self.id)


def validate_file_size(value):
    max_size = 50 * 1024 * 1024  # 50 MB

    if value.size > max_size:
        raise ValidationError(f"File size must not exceed {max_size} bytes.")


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="property_pics")
    file = models.FileField(blank=True, upload_to=property_pic_path, verbose_name="Files",
                            validators=[validate_file_size], help_text="Allowed size is 50MB", null=True)

    def __str__(self):
        return f"Image of {self.property.title}"
