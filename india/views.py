from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import data
from .serializers import OverallDataSerializer


# Create your views here.


@api_view(['GET'])
def get_current_data(request):
    current_data = data.get_current_data()
    serializer = OverallDataSerializer(current_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_timeseries_data(request):
    data_list = data.get_timeseries_data('all')
    serializer = OverallDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_timeseries_data_last_week(request):
    data_list = data.get_timeseries_data('week')
    serializer = OverallDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_timeseries_data_last_month(request):
    data_list = data.get_timeseries_data('month')
    serializer = OverallDataSerializer(data_list, many=True)
    return Response(serializer.data)
