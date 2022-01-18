from rest_framework.response import Response
from .serializers import StateDataSerializer, StateTimeseriesSerializer, StateInfoSerializer, DistrictDataSerializer
from . import data
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def get_state_info_list(request):
    info_list = data.get_state_info_list()
    serializers = StateInfoSerializer(info_list, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_info(request, code):
    state_info = data.get_state_info(code)
    serializers = StateInfoSerializer(state_info, many=False)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_data_list(request):
    data_list = data.get_all_state_data()
    serializers = StateDataSerializer(data_list, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_data(request, code):
    state_data = data.get_state_date(code)
    serializers = StateDataSerializer(state_data, many=False)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_timeseries(request, code):
    timeseries_data = data.get_timeseries(code, 'all')
    serializers = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_timeseries_last_week(request, code):
    timeseries_data = data.get_timeseries(code, 'week')
    serializers = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_state_timeseries_last_month(request, code):
    timeseries_data = data.get_timeseries(code, 'month')
    serializers = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_district_data_list(request, code):
    data_list = data.get_district_data_list(code)
    serializer = DistrictDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_data(request, code, name):
    district_data = data.get_district_data(code, name)
    serializer = DistrictDataSerializer(district_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_timeseries_data(request, code, name):
    timeseries_data = data.get_district_data_timeseries(code, name, "All")
    serializer = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_timeseries_data_week(request, code, name):
    timeseries_data = data.get_district_data_timeseries(code, name, "Week")
    serializer = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_timeseries_data_month(request, code, name):
    timeseries_data = data.get_district_data_timeseries(code, name, "Month")
    serializer = StateTimeseriesSerializer(timeseries_data, many=True)
    return Response(serializer.data)
