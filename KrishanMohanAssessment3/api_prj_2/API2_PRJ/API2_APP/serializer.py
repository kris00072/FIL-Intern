from rest_framework import serializers
from .models import API2

class API2Serializer(serializers.ModelSerializer):
    class Meta:
        model = API2
        fields = '__all__' 