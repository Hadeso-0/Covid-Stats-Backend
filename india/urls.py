from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('timeseries/',views.get_timeseries_data),
    path('timeseries/last_week', views.get_timeseries_data_last_week),
    path('timeseries/last_month', views.get_timeseries_data_last_month),
    path('current/', views.get_current_data)
]
