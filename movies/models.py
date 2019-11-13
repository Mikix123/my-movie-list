from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.timezone import now


class AgeRating(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    ageRating = models.ForeignKey(AgeRating, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=2000)
    posterUrl = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    year = models.IntegerField()
    createAt = models.DateTimeField(default=now, editable=False)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)