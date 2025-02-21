from rest_framework import generics
from .models import API2
from .serializer import API2Serializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class API2View(View):
    def post(self, request, *args, **kwargs):
        return JsonResponse({"message": "POST request received"}, status=200)



class API2ListCreateView(generics.ListCreateAPIView):
    queryset = API2.objects.all()
    serializer_class = API2Serializer


class API2DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = API2.objects.all()
    serializer_class = API2Serializer
    lookup_field = 'id' 
