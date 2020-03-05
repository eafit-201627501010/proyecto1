from rest_framework import serializers
from .models import temperature

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = ('id', 'value')