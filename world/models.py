from django.db import models


# Create your models here.

class RegionInfo(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class CountryInfo(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=5)

    def __str__(self):
        return self.code


class CountryData(models.Model):
    code = models.CharField(max_length=10, primary_key=True, default='')
    total_confirmed = models.BigIntegerField()
    daily_confirmed = models.BigIntegerField()
    total_deaths = models.BigIntegerField()
    daily_deaths = models.BigIntegerField()

    def __str__(self):
        return self.code


class CountryTimeseries(models.Model):
    date = models.DateTimeField(primary_key=True)
    total_confirmed = models.BigIntegerField()
    daily_confirmed = models.BigIntegerField()
    total_deaths = models.BigIntegerField()
    daily_deaths = models.BigIntegerField()

    def __str__(self):
        return self.date


class NewsArticle(models.Model):
    source_name = models.CharField(max_length=50)
    authors = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    news_url = models.CharField(max_length=400)
    news_image_url = models.CharField(max_length=400)
    published_time = models.DateTimeField()
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class GeneralData(models.Model):
    last_updated_time = models.DateTimeField(primary_key=True)