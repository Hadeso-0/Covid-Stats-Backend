from rest_framework import serializers
from .models import RegionInfo, CountryInfo, CountryData, CountryTimeseries


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
