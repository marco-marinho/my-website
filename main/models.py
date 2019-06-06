from django.db import models


class Education(models.Model):
    title = models.TextField()
    institution = models.TextField()
    country = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.TextField()
    authors = models.TextField()
    file = models.FileField(upload_to='papers')
    booktitle = models.TextField()
    Year = models.TextField()
    abstract = models.TextField(default=' ')

    def __str__(self):
        return self.title
