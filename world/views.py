from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import CountryDataSerializer, CountryTimeseriesSerializer, RegionDataSerializer
from . import data
from rest_framework.decorators import api_view
import json


# Create your views here.

def index(request):
    return HttpResponse("Hello World - World Stats")


@api_view(['GET'])
def get_overall_data(request):
    overall_data = data.get_country_data('Global')
    serializer = CountryDataSerializer(overall_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_data_list(request):
    data_list = data.get_country_data_list()
    serializer = CountryDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data(request, name):
    overall_data = data.get_country_data(name)
    serializer = CountryDataSerializer(overall_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_timeseries_data(request, name):
    data_list = data.get_country_timeseries_data(name, 'all')
    serializer = CountryTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_timeseries_data_week(request, name):
    data_list = data.get_country_timeseries_data(name, 'week')
    serializer = CountryTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_timeseries_data_month(request, name):
    data_list = data.get_country_timeseries_data(name, 'month')
    serializer = CountryTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_list(request):
    region_list = data.get_region_list()
    serializer = RegionDataSerializer(region_list, many=True)
    return Response(serializer.data)
