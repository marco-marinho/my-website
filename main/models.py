from django.db import models
from django.utils.timezone import now


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
    date = models.DateField(default=now)
    abstract = models.TextField(default=' ')

    def __str__(self):
        return self.title


class Research(models.Model):
    research = models.CharField(max_length=200)
    short_description = models.TextField()
    full_description = models.TextField()
    icon = models.CharField(max_length=200)
    links = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.research


class Teaching(models.Model):
    level = models.CharField(max_length=200, default='')
    topic = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.topic


class Resource(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='resources')
    description = models.TextField(default='')
    topic = models.ForeignKey(Teaching, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
