from django.urls import path
from . import views

urlpatterns = [
    path('about/app/', views.get_about_app),
    path('about/developers/', views.get_about_developer),
    path('about/source/', views.get_about_source),
    path('world/global/', views.get_global_data),
    path('world/news/', views.get_world_news),
    path('world/region/info/', views.get_who_region_info_list),
    path('world/region/info/<str:region_code>/', views.get_who_region_info),
    path('world/region/data/', views.get_who_region_data_list),
    path('world/region/data/<str:region_code>/', views.get_who_region_data),
    path('world/region/data/<str:region_code>/countries/', views.get_who_region_country_data_list),
    path('world/country/info/', views.get_country_info_list),
    path('world/country/info/<str:country_code>/', views.get_country_info),
    path('world/country/data/', views.get_country_data_list),
    path('world/country/data/<str:country_code>/', views.get_country_data),
    path('world/country/data/<str:country_code>/timeseries/', views.get_country_data_timeseries),
    path('india/', views.get_india_data),
    path('india/timeseries/', views.get_india_data_timeseries),
    path('india/news/', views.get_india_news),
    path('state/info/', views.get_state_info_list),
    path('state/info/<str:state_code>/', views.get_state_info),
    path('state/data/', views.get_state_data_list),
    path('state/data/<str:state_code>/', views.get_state_data),
    path('state/data/<str:state_code>/timeseries/', views.get_state_data_timeseries),
    path('state/data/<str:state_code>/districts/', views.get_district_data_list),
    path('state/data/<str:state_code>/districts/<str:district_name>/', views.get_district_data),
    path('state/data/<str:state_code>/districts/<str:district_name>/timeseries/', views.get_district_data_timeseries)
]
