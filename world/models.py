from django.db import models


# Create your models here.

class CountryData(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    who_region = models.CharField(max_length=40)
    total_confirmed = models.BigIntegerField()
    daily_confirmed = models.BigIntegerField()
    total_deaths = models.BigIntegerField()
    daily_deaths = models.BigIntegerField()

    def __str__(self):
        return self.name


class CountryTimeseries(models.Model):
    date = models.DateTimeField(primary_key=True)
    total_confirmed = models.BigIntegerField()
    daily_confirmed = models.BigIntegerField()
    total_deaths = models.BigIntegerField()
    daily_deaths = models.BigIntegerField()

    def __str__(self):
        return self.date


class RegionData(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
