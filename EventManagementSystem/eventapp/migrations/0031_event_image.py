# Generated by Django 5.0.6 on 2024-07-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0030_booking_last_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
