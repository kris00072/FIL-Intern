from django.urls import path,include
from .views import BlackHolesViewSet
from rest_framework import routers
vrouter = routers.DefaultRouter()

vrouter.register('blackholes',BlackHolesViewSet,basename='blackholes')

urlpatterns = vrouter.urls