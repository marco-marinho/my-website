from django.db import models
from datetime import datetime

class Education(models.Model):
    title = models.TextField()
    institution = models.TextField()
    country = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField()

class Publication(models.Model):
    title = models.TextField()
    authors = models.TextField()
    file = models.FileField(upload_to='papers')
    booktitle = models.TextField()
    Year = models.TextField()