from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Visitor(models.Model):
    vid = models.AutoField(primary_key=True)
    ip = models.CharField(unique=True, max_length=15)
    cnt = models.IntegerField(default=0)
    created_time = models.DateTimeField('updated time', default=timezone.now)

class VisitorHistory(models.Model):
    visitor = models.ForeignKey("Visitor", to_field="vid", default=1, on_delete=models.CASCADE)
    visitor_time = models.DateTimeField('visited time', default=timezone.now)
