from rest_framework import serializers
from .models import RegionInfo, CountryInfo, CountryData, CountryTimeseries, NewsArticle


class RegionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionInfo
        fields = '__all__'


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = '__all__'


class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryData
        fields = '__all__'


class CountryTimeseriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryTimeseries
        fields = '__all__'


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = (
            'source_name', 'authors', 'title', 'description', 'news_url', 'news_image_url', 'published_time', 'content')
