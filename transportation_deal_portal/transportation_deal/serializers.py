from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from transportation_deal import models
from transportation_deal.models import Vehicle

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # type = (
    #     ('T', 'Transporter'),
    #     ('C', 'Customer'),
    # )
    # profile_type = serializers.ChoiceField(choices=type)
    class Meta:
        model =User
        fields=['first_name','last_name','email','city','state','phone','pin_code','is_customer','is_transporter']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
