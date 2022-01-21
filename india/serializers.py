from rest_framework import serializers
from .models import OverallData, NewsArticle


class OverallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverallData
        fields = '__all__'


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = (
            'source_name', 'authors', 'title', 'description', 'news_url', 'news_image_url', 'published_time', 'content')
