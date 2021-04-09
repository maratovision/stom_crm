from rest_framework import serializers
from accounts.models import *


class StomProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StomProfile
        fields = '__all__'
