from rest_framework import generics
from rest_framework.response import Response
# from django.contrib.auth.models import user

from .serializers import TemperaturesSerializer
from .models import Temperatures

class ListTemperature(generics.ListCreateAPIView):
    queryset = Temperatures.objects.all()
    serializer_class = TemperaturesSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TemperaturesSerializer(queryset, many=True)
        return Response(serializer.data)