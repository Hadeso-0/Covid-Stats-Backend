from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('timeseries/',views.get_timeseries_data),
    path('current/', views.get_current_data)
]
