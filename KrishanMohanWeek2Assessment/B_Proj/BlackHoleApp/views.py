
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlackHole
from .serializer import BlackHolesSerializer

class BlackHoleList(APIView):
    def get(self,request):
        data1=BlackHole.objects.all()
        data1=BlackHolesSerializer(data1, many=True)
        return Response(data1.data)
    
    def post(self,request):
        data=BlackHolesSerializer(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

class BlackHoleDetail(APIView):
    def get(self,request,pk):
        try:
            data1=BlackHole.objects.get(Bid=pk)
            data1=BlackHolesSerializer(data1)
            return Response(data1.data)
        except BlackHole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        try:
            data1=BlackHole.objects.get(Bid=pk)
            data=BlackHolesSerializer(data1, data=request.data)
            if(data.is_valid()):
                data.save()
                return Response(data.data)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except BlackHole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk):
        try:
            data1=BlackHole.objects.get(Bid=pk)
            data1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BlackHole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


