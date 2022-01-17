from rest_framework.response import Response
from .serializers import RegionInfoSerializer, CountryInfoSerializer, CountryDataSerializer, CountryTimeseriesSerializer
from . import data
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def get_overall_data(request):
    global_data = data.get_country_data("GLOBAL")
    serializer = CountryDataSerializer(global_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_region_info_list(request):
    info_list = data.get_region_info_list()
    serializer = RegionInfoSerializer(info_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_region_info(request, code):
    info = data.get_region_info(code)
    serializer = RegionInfoSerializer(info, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_region_data(request, code):
    region_data = data.get_region_data(code)
    serializer = CountryDataSerializer(region_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_info_list(request):
    country_info_list = data.get_country_info_list()
    serializer = CountryInfoSerializer(country_info_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_info(request, code):
    country_info = data.get_country_info(code)
    serializer = CountryInfoSerializer(country_info, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_list(request):
    data_list = data.get_country_data_list()
    serializer = CountryDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data(request, code):
    country_data = data.get_country_data(code)
    serializer = CountryDataSerializer(country_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_timeseries(request, code):
    timeseries_data = data.get_country_timeseries_data(code, "all")
    serializer = CountryTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_timeseries_week(request, code):
    timeseries_data = data.get_country_timeseries_data(code, "week")
    serializer = CountryTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_timeseries_month(request, code):
    timeseries_data = data.get_country_timeseries_data(code, "month")
    serializer = CountryTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)
