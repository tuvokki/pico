import datetime

from django.db import models
from django.utils import timezone


class Hero(models.Model):
    image = models.FileField(upload_to='hero_images/')
    head  = models.CharField(max_length=200)
    sub  = models.CharField(max_length=200)
    link  = models.URLField(max_length=200)
    linktext  = models.CharField(max_length=200)
    slot  = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.head

class IconCard(models.Model):
    icon  = models.CharField(max_length=200)
    headline  = models.CharField(max_length=200)
    body  = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slot  = models.CharField(max_length=2000)

    def __str__(self):
        return self.headline

class InfoCard(models.Model):
    headline  = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slot  = models.CharField(max_length=2000)

    def __str__(self):
        return self.headline
