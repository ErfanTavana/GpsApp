from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['user', 'latitude', 'longitude', 'timestamp', 'timestamp_shamsi', 'speed', 'battery_level']
