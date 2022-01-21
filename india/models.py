from django.db import models


# Create your models here.

class OverallData(models.Model):
    date = models.DateTimeField(primary_key=True)
    total_confirmed = models.BigIntegerField()
    daily_confirmed = models.BigIntegerField()
    total_recovered = models.BigIntegerField()
    daily_recovered = models.BigIntegerField()
    total_deceased = models.BigIntegerField()
    daily_deceased = models.BigIntegerField()

    def __str__(self):
        return f"India - {self.date}"

    def is_empty(self):
        if self.daily_confirmed == "0" or self.daily_confirmed == 0:
            return True
        return False


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
