# Generated by Django 5.0.6 on 2024-07-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0035_remove_foodpackage_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpackage',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
