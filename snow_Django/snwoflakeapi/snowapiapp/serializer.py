from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('trip_id', 'trip_name', 'trip_cost')
