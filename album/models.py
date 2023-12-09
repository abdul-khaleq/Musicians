from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    albumName = models.CharField(max_length=55)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    albumReleaseDate = models.DateTimeField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Album name: {self.albumName}"