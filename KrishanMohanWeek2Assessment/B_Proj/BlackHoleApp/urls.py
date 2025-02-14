from django.urls import path,include
from . import views

urlpatterns = [
    path('blackholes/',views.BlackHoleList.as_view(),name='blackholes'),
    path('blackholes/<int:pk>/',views.BlackHoleDetail.as_view(),name='blackhole_detail'),
]