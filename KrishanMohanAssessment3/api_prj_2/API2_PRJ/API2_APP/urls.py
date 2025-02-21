
from django.urls import path
from .views import API2ListCreateView, API2DetailView

urlpatterns = [
    path('location/', API2ListCreateView.as_view(), name='api1-list-create'),
    path('location/<int:id>/', API2DetailView.as_view(), name='api1-detail'),
]
