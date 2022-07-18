from django.db import models

    

# Create your models here.
class Songs(models.Model):
 artist_name = models.CharField(max_length=100)
 duration = models.IntegerField()
 song_title = models.CharField(max_length=100)
 
class platforma(models.Model):
    platfrom = models.ForeignKey(Songs,on_delete=models.CASCADE)
    platformname = models.CharField(max_length=100)
 
