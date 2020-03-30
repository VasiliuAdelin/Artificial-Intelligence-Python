from django.db import models
    
class Ratings(models.Model):
    movieId = models.IntegerField()
    rating = models.FloatField()

class Tags(models.Model):
    movieID = models.IntegerField()
    tag = models.CharField(max_length=200)

class Movies(models.Model):
    movieID = models.IntegerField()
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)

class Links(models.Model):
    movieID = models.IntegerField()
    imbdLink = models.CharField(max_length=200)
    tmdbLink = models.CharField(max_length=200)

# class MovieDet:
#     def __init__(self, movieTitle, movieLink):  
#     movieTitle : str
#     movieLink : str