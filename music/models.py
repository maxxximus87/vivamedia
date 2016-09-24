from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album  = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_file = models.FileField()


    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.album_id})

class Image(models.Model):
    image_title = models.CharField(max_length=250)
    image_file = models.FileField()

    def __str__(self):
        return self.image_title

    def get_absolute_url(self):
        return reverse('music:images')

class Video(models.Model):
    video_title = models.CharField(max_length=250)
    video_file = models.FileField()

    def __str__(self):
        return self.video_title

    def get_absolute_url(self):
        return reverse('music:videos')