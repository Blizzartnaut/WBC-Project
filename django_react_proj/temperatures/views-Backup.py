from time import strftime
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from rest_framework import generics
# from django.views.generic.dates import DayArchiveView
from django.views.generic import ListView
from rest_framework import filters
#from rest_framework.filters import SearchFilter
from django.db.models import Q

from .models import Temperatures
from .serializers import *

## these are modeled after the documentation

class TempListView(ListView):
    model = Temperatures

    def head(self, *args, **kwargs):
        last_temp = self.get_queryset().latest('sub_date')
        response = HttpResponse()
        #RFC 1123 date format (from documentation)
        response['Last-Modified'] = last_temp.sub_date,strftime('%a, %d, %b, %Y, %H:%M:%S GMT')
        return response

## Keeping after in case of failure, trying to get it right

# #class DynamicSearchFilter(filters.SearchFilter):
#     #def get_search_fields(self, view, request):
#     #    return request.GET.getlist('search_fields', [])

# '''class DateUpkeep(generics.ListCreateAPIView):
#     queryset = Temperatures.objects.all()
#     serializer_class = TemperaturesSerializer
#     filter_backends = [filters.SearchFilter]'''

# '''class DateUpkeep(generics.ListCreateAPIView):
#     serializer_class = TemperaturesSerializer

#     def get_queryset(self):
#         date = self.kwargs['date']
#         return Temperatures.objects.filter(temperature__date='date')'''


# class TemperatureList(generics.ListAPIView):
#     model = Temperatures
#     serializer_class = TemperaturesSerializer

#     def get_queryset(self): #_queryset
#         """
#         Optionally restricts the returned temperatures to a given date,
#         by filtering against a `date` query parameter in the URL.
#         """
#         query = self.request.GET.get('date', '2021-04-03')
#         object_list = Temperatures.objects.filter(
#             Q(date__icontains=query)
#         )
#         return object_list

# #Create your views here.
# #@api_view(['GET',])
# #def temperatures_search(request):

## Should recieve and post to the database

@api_view(['GET','POST'])
def temperatures_list(request):
    serializer = TemperaturesSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status = status.HTTP_201_CREATED)
        
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def temperatures_detail(request, pk):
#     try:
#         temperature = Temperatures.objects.get(pk=pk)
#     except Temperatures.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         serializer = TemperaturesSerializer(temperature, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status = status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         temperature.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)