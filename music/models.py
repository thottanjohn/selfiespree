# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=250)						
    genre=models.CharField(max_length=250)
    album_logo=models.FileField()
    def __str__(self):
        return self.album_title + '-' + self.artist
    def get_absolute_url(self):
        return reverse('music:music_detail',kwargs={'pk':self.pk})

