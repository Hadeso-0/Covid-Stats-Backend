from rest_framework import serializers
from .models import StateData, StateTimeseriesData, StateInfo


class StateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateInfo
        fields = '__all__'


class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateData
        fields = '__all__'


class StateTimeseriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateTimeseriesData
        fields = '__all__'
