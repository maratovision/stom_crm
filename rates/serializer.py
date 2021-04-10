from rest_framework import serializers
from .models import *


class RateSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rate
        fields = ['id', 'client', 'doctor', 'mark', 'comment']


class RateCreateSerializer(serializers.Serializer):
    mark = serializers.IntegerField(min_value=0, max_value=5)