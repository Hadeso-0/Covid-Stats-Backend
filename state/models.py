from django.db import models


# Create your models here.

class StateData(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    confirmed = models.BigIntegerField()
    recovered = models.BigIntegerField()
    deceased = models.BigIntegerField()
    active = models.BigIntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name


class StateTimeseriesData(models.Model):
    date = models.DateTimeField(primary_key=True)
    confirmed = models.BigIntegerField()
    recovered = models.BigIntegerField()
    deceased = models.BigIntegerField()
    active = models.BigIntegerField()

    def __str__(self):
        return self.date
