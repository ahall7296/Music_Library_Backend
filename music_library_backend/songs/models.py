from django.db import models
# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    album=models.CharField(max_length=250)
    release_date=models.DateField(auto_now_add=True)
    genre=models.CharField(max_length=250)
    like=models.IntegerField(default=0)