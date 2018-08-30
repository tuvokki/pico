from django.db import models


class Joke(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    punchline = models.TextField()
    pub_date = models.DateTimeField('date_published')
    
    def __str__(self):
        return self.title
