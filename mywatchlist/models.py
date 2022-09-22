from django.db import models

class WatchlistItem(models.Model):
    watched = models.CharField(max_length=50)
    title = models.TextField()
    rating = models.IntegerField()
    release_date =  models.DateField()
    review = models.TextField()