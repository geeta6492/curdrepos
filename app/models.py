from django.db import models

# Create your models here.
class Album(models.Model):
    aname = models.CharField(max_length=100)

class Song(models.Model):
    sname = models.CharField(max_length=100)
    albums = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='album_song')

class Artist(models.Model):
    artname = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song,related_name='song_artist')


# album-song 1-m
# artist-song m-m
# album-artist