from django.contrib import admin
from .models import NewsArticle, Properties, Developer, AboutApp

# Register your models here.

admin.site.register(NewsArticle)
admin.site.register(Properties)
admin.site.register(Developer)
admin.site.register(AboutApp)