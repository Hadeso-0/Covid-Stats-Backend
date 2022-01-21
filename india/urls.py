from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_current_data),
    path('timeseries/', views.get_timeseries_data),
    path('timeseries/last_week', views.get_timeseries_data_last_week),
    path('timeseries/last_month', views.get_timeseries_data_last_month),
    path('news/', views.get_news_headlines)
]
