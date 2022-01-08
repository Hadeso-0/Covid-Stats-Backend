from django.db import models


# Create your models here.

class StateInfo(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"State Info - {self.code}"


class StateData(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    confirmed = models.BigIntegerField()
    recovered = models.BigIntegerField()
    deceased = models.BigIntegerField()
    active = models.BigIntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return f"State - {self.code}"


class StateTimeseriesData(models.Model):
    date = models.DateTimeField(primary_key=True)
    confirmed = models.BigIntegerField()
    recovered = models.BigIntegerField()
    deceased = models.BigIntegerField()
    active = models.BigIntegerField()

    def __str__(self):
        return f"State Timeseries - {self.date}"
