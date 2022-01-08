from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.get_state_info_list),
    path('info/<str:code>/', views.get_state_info),
    path('', views.get_state_data_list),
    path('<str:code>/', views.get_state_data),
    path('<str:code>/timeseries/', views.get_state_timeseries),
    path('<str:code>/timeseries/last_week/', views.get_state_timeseries_last_week),
    path('<str:code>/timeseries/last_month/', views.get_state_timeseries_last_month)
]
