from __future__ import unicode_literals

from django.db import models

# Create your models here.
#RED pk 1
class Album(models.Model):
	artist = models.CharField(max_lenght=250)
	album_title =models.CharField(max_lenght=250)
	genre = models.CharField(max_lenght=100)
	album_logo = models.CharField(max_lenght=1000)

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_lenght=10)
	song_title = models.CharField(max_lenght=250)	