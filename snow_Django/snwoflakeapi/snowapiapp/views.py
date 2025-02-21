from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Trip
from .serializer import TripSerializer,TripLimitedSerializer
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TripListCreateAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class TripRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated] 

class TripDetails(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripLimitedSerializer 

class TripDetailsByDate(APIView):
    def post(self, request):
        trip_date = request.data.get("date", None)  # Get date from JSON body

        if not trip_date:
            return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)

        parsed_date = parse_date(trip_date)  # Convert string to date object
        if not parsed_date:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        trips = Trip.objects.filter(Q(start_date=parsed_date) | Q(end_date=parsed_date))  # Filter by start or end date
        serializer = TripSerializer(trips, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)