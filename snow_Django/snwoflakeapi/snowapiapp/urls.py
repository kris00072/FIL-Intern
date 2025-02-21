from django.urls import path
from .views import TripListCreateAPIView, TripRetrieveUpdateDestroyAPIView,TripDetails,TripDetailsByDate

urlpatterns = [
    path('trips/', TripListCreateAPIView.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', TripRetrieveUpdateDestroyAPIView.as_view(), name='trip-detail'),
    path('trip-details-by-date/', TripDetailsByDate.as_view(), name='trip-details-by-date'),
]
