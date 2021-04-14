from rest_framework import serializers
from temperatures.models import Temperatures
from django.db import models

class TemperaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperatures
        fields = ['pk', 'date', 'time', 'burnerzone', 'burner_1', 'burner_2', 'burner_3', 'burner_4', 'burner_5', 'burner_6', 'burner_7', 'burner_8', 'burner_9', 'burner_10', 'burner_11', 'burner_12', 'user']
        