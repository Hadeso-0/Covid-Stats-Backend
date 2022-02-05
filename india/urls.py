from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_current_data),
    path('timeseries/', views.get_timeseries_data),
    path('news/', views.get_news_headlines)
]
