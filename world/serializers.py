from rest_framework import serializers
from .models import CountryData, CountryTimeseries


class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryData
        fields = '__all__'


class CountryTimeseriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryTimeseries
        fields = '__all__'
