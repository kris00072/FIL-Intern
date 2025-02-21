from rest_framework import serializers
from .models import API1

class API1Serializer(serializers.ModelSerializer):
    class Meta:
        model = API1
        fields = '__all__' 
