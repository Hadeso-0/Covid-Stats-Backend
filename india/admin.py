from django.contrib import admin

from .models import OverallData, NewsArticle, GeneralData

# Register your models here.

admin.site.register(NewsArticle)
admin.site.register(GeneralData)