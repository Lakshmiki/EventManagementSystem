# Generated by Django 5.0.6 on 2024-07-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0032_foodpackage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpackage',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
