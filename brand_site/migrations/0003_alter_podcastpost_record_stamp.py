# Generated by Django 4.2.8 on 2024-01-01 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_site', '0002_podcastpost_podcaster_podcastpost_record_stamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastpost',
            name='record_stamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]