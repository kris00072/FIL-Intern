from rest_framework import generics
from .models import API1
from .serializer import API1Serializer
import requests
from django.http import JsonResponse


class API1ListCreateView(generics.ListCreateAPIView):
    queryset = API1.objects.all()
    serializer_class = API1Serializer

class API1DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = API1.objects.all()
    serializer_class = API1Serializer
    lookup_field = 'item_id' 


import requests
from django.http import JsonResponse
from .models import API1

def get_data(request):
    prices = API1.objects.all()
    price_data = API1Serializer(prices, many=True).data  # Serialize queryset

    try:
        response = requests.get("http://127.0.0.1:8000/location/")
        location_data = response.json() if response.status_code == 200 else {"error": "Failed to fetch location data"}
    except requests.exceptions.RequestException:
        location_data = {"error": "location service unavailable"}

    return JsonResponse({"prices": price_data, "location": location_data}, safe=False)
