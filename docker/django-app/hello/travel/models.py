import datetime

from django.db import models
from django.utils import timezone


class Country(models.Model):
    name_text = models.CharField(max_length=200, primary_key=True)
    last_changed_date = models.DateTimeField('date changed', default=timezone.now)

    def __str__(self):
        return str(self.name_text)

    def recently_updated(self):
        return self.last_changed_date >= timezone.now() - datetime.timedelta(days=1)


class CountryRestriction(models.Model):
    restricting_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200, null=True)
    last_changed_date = models.DateTimeField('date changed', default=timezone.now)
    allow_unvaccinated = models.BooleanField(default=True)
    banned = models.BooleanField(default=False)
    restricted = models.BooleanField(default=False)
    quarantine_days = models.IntegerField(default=0)
    restrictions_text = models.TextField()

    def __str__(self):
        return str(self.name_text)

    def recently_updated(self):
        return self.last_changed_date >= timezone.now() - datetime.timedelta(days=1)
