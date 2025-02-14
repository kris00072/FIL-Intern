from rest_framework import serializers
from . import models

class BlackHolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlackHole
        fields = '__all__'

