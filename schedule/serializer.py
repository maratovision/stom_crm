from rest_framework import serializers
from .models import *


class DrTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrTime
        fields = '__all__'



