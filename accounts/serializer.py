from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from accounts.models import *


class StomProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StomProfile
        fields = '__all__'


class SighUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16)
    confirm_password = serializers.CharField(min_length=8, max_length=16, write_only=True)
    date_birth = serializers.DateField(write_only=True)
    gender = serializers.ChoiceField(choices=(
        ('male', 'male'),
        ('female', 'female')
    ), write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password',
                  'confirm_password', 'date_birth', 'gender']


    def create(self, validate_data):
        password = validate_data.pop('password')
        confirm_password = validate_data.pop('confirm_password')
        date_birth = validate_data.pop('date_birth')
        gender = validate_data.pop('gender')
        if password != confirm_password:
            raise ValidationError({'data': 'password dont match'})
        user = User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user= user, date_birth= date_birth , gender= gender,
                                   full_name= user.first_name.capitalize() + ' ' + user.last_name.capitalize())
        return user
