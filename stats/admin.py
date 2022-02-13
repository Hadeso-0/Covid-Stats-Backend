from django.contrib import admin
from .models import AboutApp, Developer, DataSource

# Register your models here.

admin.site.register(AboutApp)
admin.site.register(Developer)
admin.site.register(DataSource)