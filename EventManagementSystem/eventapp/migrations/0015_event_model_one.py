# Generated by Django 5.0.6 on 2024-06-26 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0014_vendor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_model_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('Marriage', 'Marriage'), ('Dance Show', 'Dance Show'), ('Birthday Party', 'Birthday Party'), ('College Festival', 'College Festival')], max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('place', models.CharField(max_length=255)),
                ('equipment', models.TextField()),
                ('booking_id', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.vendor')),
            ],
        ),
    ]
