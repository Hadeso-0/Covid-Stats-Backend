from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_states),
    path('<str:state>', views.get_state_data),
    path('<str:state>/timeseries', views.get_state_timeseries),
    path('<str:state>/timeseries/last_week', views.get_state_timeseries_last_week),
    path('<str:state>/timeseries/last_month', views.get_state_timeseries_last_month)
]
