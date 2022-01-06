from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import OverallDataSerializer
from . import data
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    return HttpResponse("Hello World - India Stats")


@api_view(['GET'])
def get_timeseries_data(request):
    data_list = data.get_timeseries_data()
    serializer = OverallDataSerializer(data_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_current_data(request):
    current_data = data.get_current_data()
    serializer = OverallDataSerializer(current_data, many=False)
    return Response(serializer.data)
