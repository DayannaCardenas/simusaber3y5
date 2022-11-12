#codigo propio
from apps.profiles.apiViews import *
from apps.locations.serializers import *

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response

from django.db.models import F

@api_view(['GET'])
def api_departament(request):
    if request.method== 'GET':
        queryset = Departament.objects.filter(country=request.query_params.get('country'))
        serializer = DepartamentSerializer(queryset, many=True)
        return Response(serializer.data, status=200)      

@api_view(['GET'])
def api_city(request):
    if request.method== 'GET':
        queryset = City.objects.filter(departament=request.query_params.get('departament'))
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def api_office(request, pk=None):
    if request.method== 'GET':
        if pk:
            queryset = Office.objects.filter(id=pk)
            queryset=queryset.annotate(city_name=F("office__city__name"), departament_name=F("office__city__departament__name"), country=F("office__city__departament__country"))
        elif request.query_params.get('city')!=None:
            queryset = Office.objects.filter(city=request.query_params.get('city'))
        else:
            return Response({"error":"error"}, status=400)
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data, status=200) 