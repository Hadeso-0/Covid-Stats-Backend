from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_overall_data),
    path('country', views.get_data_list),
    path('country/<str:name>', views.get_country_data)
]
