from django.db import models
from datetime import datetime
# Create your models here.
class data(models.Model):
    title = models.CharField( max_length=150)
    body = models.CharField(max_length=100000000)
    date = models.DateTimeField(default=datetime.now,blank=True)

