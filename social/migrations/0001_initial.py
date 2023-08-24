# Generated by Django 4.2.3 on 2023-08-24 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(blank=True, max_length=200, null=True)),
                ('sender_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender_number', models.CharField(blank=True, max_length=15, null=True)),
                ('message_text', models.TextField(blank=True, null=True)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
