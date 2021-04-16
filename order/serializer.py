from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = '__all__'


class OrderHardSerializer(serializers.Serializer):
    reason = serializers.CharField(max_length=50)