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
