# Generated by Django 5.0.6 on 2024-06-30 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0025_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]
