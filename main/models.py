from django.db import models

# Create your models here.



class Film(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    rating = models.FloatField()
    duration = models.FloatField()

    def __str__(self):
        return self.name