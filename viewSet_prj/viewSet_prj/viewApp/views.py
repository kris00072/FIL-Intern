from django.shortcuts import render,HttpResponse
from .serializer import BlackHolesSerializer
from .models import BlackHoles
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class BlackHolesViewSet(viewsets.ViewSet): 
    def list(self, request):
        data1=BlackHoles.objects.all()
        data1=BlackHolesSerializer(data1, many=True)
        return Response(data1.data)
    
    def create(self, request):
        data=BlackHolesSerializer(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            data1=BlackHoles.objects.get(id=pk)
            data1=BlackHolesSerializer(data1)
            return Response(data1.data)
        except BlackHoles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            data1=BlackHoles.objects.get(id=pk)
            data=BlackHolesSerializer(data1, data=request.data)
            if(data.is_valid()):
                data.save()
                return Response(data.data)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except BlackHoles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            data1=BlackHoles.objects.get(id=pk)
            data1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BlackHoles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



