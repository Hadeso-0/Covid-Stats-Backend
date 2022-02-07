from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from . import news_manager as news_mgr
from . import data_manager_world as world_mgr
from . import data_manager_india as india_mgr
from . import data_manager_state as state_mgr
from .enums import RegionType

import uuid


@api_view(['GET'])
def get_global_data(request):
    global_data = world_mgr.get_global_data()
    serializer = serializers.GlobalDataSerializer(global_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_world_news(request):
    news_data = news_mgr.get_top_headlines(RegionType.GLOBAL)
    serializer = serializers.NewsArticleSerializer(news_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_info_list(request):
    info_list = world_mgr.get_region_info_list()
    serializer = serializers.WhoRegionInfoSerializer(info_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_info(request, region_code):
    info = world_mgr.get_region_info(region_code)
    serializer = serializers.WhoRegionInfoSerializer(info, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_data_list(request):
    data_list = world_mgr.get_region_data_list()
    serializer = serializers.WhoRegionDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_data(request, region_code):
    data = world_mgr.get_region_data(region_code)
    serializer = serializers.WhoRegionDataSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_who_region_country_data_list(request, region_code):
    data_list = world_mgr.get_region_country_data_list(region_code)
    serializer = serializers.CountryDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_info_list(request):
    info_list = world_mgr.get_country_info_list()
    serializer = serializers.CountryInfoSerializer(info_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_info(request, country_code):
    info = world_mgr.get_country_info(country_code)
    serializer = serializers.CountryInfoSerializer(info, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_list(request):
    data_list = world_mgr.get_country_data_list()
    serializer = serializers.CountryDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data(request, country_code):
    data = world_mgr.get_country_data(country_code)
    serializer = serializers.CountryDataSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_country_data_timeseries(request, country_code):
    data_timeseries = world_mgr.get_country_timeseries_data(country_code)
    serializer = serializers.CountryTimeSeriesDataSerializer(data_timeseries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_india_data(request):
    data = india_mgr.get_overall_data()
    serializer = serializers.IndiaDataSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_india_data_timeseries(request):
    data = india_mgr.get_timeseries_data()
    serializer = serializers.IndiaDataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_india_news(request):
    news_data = news_mgr.get_top_headlines(RegionType.INDIA)
    serializer = serializers.NewsArticleSerializer(news_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_info_list(request):
    info_list = state_mgr.get_state_info_list()
    serializer = serializers.StateInfoSerializer(info_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_info(request, state_code):
    info = state_mgr.get_state_info(state_code)
    serializer = serializers.StateInfoSerializer(info, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_data_list(request):
    data_list = state_mgr.get_all_state_data()
    serializer = serializers.StateDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_data(request, state_code):
    data = state_mgr.get_state_date(state_code)
    serializer = serializers.StateDataSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_data_timeseries(request, state_code):
    data = state_mgr.get_state_timeseries(state_code)
    serializer = serializers.StateDataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_data_list(request, state_code):
    data = state_mgr.get_district_data_list(state_code)
    serializer = serializers.DistrictDataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_data(request, state_code, district_name):
    data = state_mgr.get_district_data(state_code, district_name)
    serializer = serializers.DistrictDataSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_data_timeseries(request, state_code, district_name):
    data = state_mgr.get_district_data_timeseries(state_code, district_name)
    serializer = serializers.DistrictTimeSeriesDataSerializer(data, many=True)
    return Response(serializer.data)
