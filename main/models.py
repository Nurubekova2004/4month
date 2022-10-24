from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    rating = models.FloatField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE )

    def __str__(self):
        return self.name






