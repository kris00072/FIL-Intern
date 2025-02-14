from django.shortcuts import render, HttpResponse
from .serializer import QuestionsSerializer
from .models import Questions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class QuestionsViewSet(viewsets.ViewSet): 
    def list(self, request):
        data1 = Questions.objects.all()
        data1 = QuestionsSerializer(data1, many=True)
        return Response(data1.data)
    
    def create(self, request):
        data = QuestionsSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            data1 = Questions.objects.get(qno=pk)
            data1 = QuestionsSerializer(data1)
            return Response(data1.data)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            data1 = Questions.objects.get(qno=pk)
            data = QuestionsSerializer(data1, data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            data1 = Questions.objects.get(qno=pk)
            data1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
