from django.contrib import admin
from .models import StateInfo, StateData, StateTimeseriesData

# Register your models here.

admin.site.register(StateInfo)
admin.site.register(StateData)
admin.site.register(StateTimeseriesData)
