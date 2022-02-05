from rest_framework import serializers
from .models import CovidStats, NewsArticle, WhoRegionInfo, CountryInfo, StateInfo


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = (
            'source_name',
            'authors',
            'title',
            'description',
            'news_url',
            'news_image_url',
            'published_time',
            'content'
        )


class GlobalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'total_confirmed',
            'daily_confirmed',
            'total_deceased',
            'daily_deceased'
        )


class WhoRegionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoRegionInfo
        fields = (
            'region_code_who',
            'region_name_who'
        )


class WhoRegionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'region_code_who',
            'region_name_who',
            'total_confirmed',
            'daily_confirmed',
            'total_deceased',
            'daily_deceased'
        )


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = (
            'region_code_who',
            'region_name_who',
            'country_code',
            'country_name'
        )


class CountryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'region_code_who',
            'region_name_who',
            'country_code',
            'country_name',
            'total_confirmed',
            'daily_confirmed',
            'total_deceased',
            'daily_deceased'
        )


class CountryTimeSeriesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'region_code_who',
            'region_name_who',
            'country_code',
            'country_name',
            'date_of_stat',
            'total_confirmed',
            'daily_confirmed',
            'total_deceased',
            'daily_deceased'
        )


class IndiaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'date_of_stat',
            'total_confirmed',
            'daily_confirmed',
            'total_recovered',
            'daily_recovered',
            'total_deceased',
            'daily_deceased',
            'total_active',
            'daily_active'
        )


class StateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateInfo
        fields = (
            'state_code',
            'state_name',
        )


class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'state_code',
            'state_name',
            'total_confirmed',
            'daily_confirmed',
            'total_recovered',
            'daily_recovered',
            'total_deceased',
            'daily_deceased',
            'total_active',
            'daily_active'
        )


class StateTimeSeriesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'state_code',
            'state_name',
            'date_of_stat',
            'total_confirmed',
            'daily_confirmed',
            'total_recovered',
            'daily_recovered',
            'total_deceased',
            'daily_deceased',
            'total_active',
            'daily_active'
        )


class DistrictDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'state_code',
            'state_name',
            'district_name',
            'total_confirmed',
            'daily_confirmed',
            'total_recovered',
            'daily_recovered',
            'total_deceased',
            'daily_deceased',
            'total_active',
            'daily_active'
        )


class DistrictTimeSeriesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = (
            'region_type',
            'state_code',
            'state_name',
            'district_name',
            'date_of_stat',
            'total_confirmed',
            'daily_confirmed',
            'total_recovered',
            'daily_recovered',
            'total_deceased',
            'daily_deceased',
            'total_active',
            'daily_active'
        )
