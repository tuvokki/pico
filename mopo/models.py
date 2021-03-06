import datetime

from django.db import models
from django.utils import timezone


class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.quote_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
