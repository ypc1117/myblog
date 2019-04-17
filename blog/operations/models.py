from django.db import models
import django.utils.timezone as timezone 

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    created_time = models.DateTimeField('created time', default=timezone.now)

class BlogComment(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    comment = models.CharField(max_length=400)
    blog = models.ForeignKey("Blog", to_field="id", on_delete=models.CASCADE)
    created_time = models.DateTimeField('created time', default=timezone.now)

    
