from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import data, news
from .serializers import OverallDataSerializer, NewsArticleSerializer


# Create your views here.

@api_view(['GET'])
def get_news_headlines(request):
    news_data = news.get_top_headlines()
    serializer = NewsArticleSerializer(news_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_current_data(request):
    current_data = data.get_current_data()
    serializer = OverallDataSerializer(current_data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_timeseries_data(request):
    data_list = data.get_timeseries_data()
    serializer = OverallDataSerializer(data_list, many=True)
    return Response(serializer.data)