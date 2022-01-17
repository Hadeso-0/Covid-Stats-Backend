from django.contrib import admin
from .models import RegionInfo, CountryInfo, CountryData, CountryTimeseries

# Register your models here.

admin.site.register(RegionInfo)
admin.site.register(CountryInfo)
admin.site.register(CountryData)
admin.site.register(CountryTimeseries)
