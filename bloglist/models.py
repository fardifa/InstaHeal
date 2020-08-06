from django.db import models
from datetime import datetime
# Create your models here.

class Bloglist(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=datetime.now(), blank=True)
    body = models.TextField(default="start writing here")
