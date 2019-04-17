# Generated by Django 2.1.7 on 2019-04-14 06:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='visited time')),
            ],
        ),
        migrations.RemoveField(
            model_name='visitorcounter',
            name='visitor',
        ),
        migrations.AddField(
            model_name='visitor',
            name='cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='VisitorCounter',
        ),
        migrations.AddField(
            model_name='visitorhistory',
            name='visitor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='statistic.Visitor'),
        ),
    ]
