# Generated by Django 2.1.7 on 2019-04-13 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 8, 41, 49, 730899, tzinfo=utc), verbose_name='updated time'),
        ),
    ]
