from rest_framework import serializers
from django.contrib.auth.models import *
from apps.locations.models import *


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(read_only=True)
    departament_name = serializers.CharField(read_only=True)
    country = serializers.IntegerField(read_only=True)
    class Meta:
        model = Office
        fields = '__all__'