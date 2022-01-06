from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import StateDataSerializer, StateTimeseriesSerializer
from . import data
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    return HttpResponse("Hello World - State Stats")


@api_view(['GET'])
def get_all_states(request):
    data_list = data.get_all_state_data()
    serializer = StateDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_data(request, state):
    state_data = data.get_individual_state_date(state)
    serializer = StateDataSerializer(state_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_timeseries(request, state):
    data_list = data.get_timeseries(state, 'all')
    serializer = StateTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_timeseries_last_week(request, state):
    data_list = data.get_timeseries(state, 'week')
    serializer = StateTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_state_timeseries_last_month(request, state):
    data_list = data.get_timeseries(state, 'month')
    serializer = StateTimeseriesSerializer(data_list, many=True)
    return Response(serializer.data)
