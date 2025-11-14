from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=60, null=False)
    director_name = models.CharField(max_length=80, null=False)
    publication_year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return f"{self.title} {self.publication_year}"