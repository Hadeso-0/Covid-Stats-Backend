from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_overall_data),
    path('news/', views.get_news),
    path('region/info/', views.get_region_info_list),
    path('region/info/<str:code>/', views.get_region_info),
    path('region/data/<str:code>/', views.get_region_data),
    path('country/info/', views.get_country_info_list),
    path('country/info/<str:code>/', views.get_country_info),
    path('country/data/', views.get_country_data_list),
    path('country/data/<str:code>/', views.get_country_data),
    path('country/data/<str:code>/timeseries/', views.get_country_data_timeseries),
    path('country/data/<str:code>/timeseries/last_week', views.get_country_data_timeseries_week),
    path('country/data/<str:code>/timeseries/last_month', views.get_country_data_timeseries_month)
]
