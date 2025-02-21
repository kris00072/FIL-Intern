
from django.urls import path
from .views import API1ListCreateView, API1DetailView
from . import views

urlpatterns = [
    path('items/', API1ListCreateView.as_view(), name='api1-list-create'),
    path('items/<int:item_id>/', API1DetailView.as_view(), name='api1-detail'),
    path('data/',views.get_data),
]
