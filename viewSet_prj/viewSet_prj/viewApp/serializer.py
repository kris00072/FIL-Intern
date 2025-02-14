from rest_framework import serializers
from .models import BlackHoles

class BlackHolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackHoles
        fields = '__all__'