# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

# Create your models here.
class Picture(models.Model):
    user   = models.ForeignKey(User)
    name   = models.CharField(max_length=250)
    image  = models.FileField()
    like   = models.IntegerField(default=0)
    def get_absolute_url(self):
            return reverse('home') 

#def create_profile(sender,**kwargs):
    #if kwargs['created']:
     #   user_profile=UserProfile.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile,sender=User)    
