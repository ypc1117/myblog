# Generated by Django 2.1.7 on 2019-04-13 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=500)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated time')),
            ],
        ),
    ]