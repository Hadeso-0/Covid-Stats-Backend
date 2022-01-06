from rest_framework import serializers
from .models import OverallData


class OverallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverallData
        fields = '__all__'
