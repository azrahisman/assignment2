from django.db import models

class WatchlistItem(models.Model):
    watched = models.CharField(max_length=50) # can be changed to Boolean
    title = models.TextField() # should be changed to Char
    rating = models.IntegerField() # should limit for validity
    release_date =  models.DateField()
    review = models.TextField()