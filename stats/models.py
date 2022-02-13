from django.db import models


# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=100, default="")
    tags = models.CharField(max_length=400, default="")
    linkedin = models.CharField(max_length=400, default="")
    behance = models.CharField(max_length=400, default="")
    github = models.CharField(max_length=400, default="")
    mail = models.CharField(max_length=400, default="")
    image_url = models.CharField(max_length=400, default="")


class AboutApp(models.Model):
    app_link = models.CharField(max_length=400, default="")


class WhoRegionInfo(models.Model):
    region_code_who = models.CharField(primary_key=True, max_length=10, default="")
    region_name_who = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.region_code_who}"


class CountryInfo(models.Model):
    region_code_who = models.CharField(max_length=10, default="")
    region_name_who = models.CharField(max_length=100, default="")
    country_code = models.CharField(primary_key=True, max_length=10, default="")
    country_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.country_code}"


class StateInfo(models.Model):
    state_code = models.CharField(primary_key=True, max_length=5, default="")
    state_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.state_code}"


class CovidStats(models.Model):
    region_type = models.CharField(max_length=10, default="")

    region_code_who = models.CharField(max_length=10, default="")
    region_name_who = models.CharField(max_length=100, default="")
    country_code = models.CharField(max_length=10, default="")
    country_name = models.CharField(max_length=100, default="")
    state_code = models.CharField(max_length=5, default="")
    state_name = models.CharField(max_length=100, default="")
    district_name = models.CharField(max_length=100, default="")

    date_of_stat = models.DateTimeField()

    total_confirmed = models.BigIntegerField(default=0)
    daily_confirmed = models.BigIntegerField(default=0)
    total_recovered = models.BigIntegerField(default=0)
    daily_recovered = models.BigIntegerField(default=0)
    total_deceased = models.BigIntegerField(default=0)
    daily_deceased = models.BigIntegerField(default=0)
    total_active = models.BigIntegerField(default=0)
    daily_active = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.date_of_stat} {self.region_type} {self.region_code_who} {self.country_code} {self.state_code}" \
               + f"{self.district_name} "


class NewsArticle(models.Model):
    region_type = models.CharField(max_length=10, default="")
    source_name = models.CharField(max_length=50, default="")
    authors = models.CharField(max_length=300, default="")
    title = models.CharField(max_length=300, default="")
    description = models.CharField(max_length=1000, default="")
    news_url = models.CharField(max_length=400, default="")
    news_image_url = models.CharField(max_length=400, default="")
    published_time = models.DateTimeField()
    content = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.title


class Properties(models.Model):
    india_news_last_updated_time = models.DateTimeField(null=True)
    world_news_last_updated_time = models.DateTimeField(null=True)


class ThreadSafe(models.Model):
    key = models.CharField(max_length=200, unique=True)
