from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_overall_data),
    path('country', views.get_data_list),
    path('country/<str:name>', views.get_country_data),
    path('country/<str:name>/timeseries',views.get_country_timeseries_data),
    path('country/<str:name>/timeseries/week', views.get_country_timeseries_data_week),
    path('country/<str:name>/timeseries/month', views.get_country_timeseries_data_month),
]
