import datetime
from django.db import models

# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    album=models.CharField(max_length=250)
    release_date=models.DateField(default=datetime.date.today)
    genre=models.CharField(max_length=250)
    like=models.IntegerField(default=0)