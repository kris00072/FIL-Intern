from django.urls import path
from .views import (
    HomeView, RegisterView, CustomLoginView, CustomLogoutView, DashboardView, 
    AddStockView, UpdateStockView, DeleteStockView
)

urlpatterns = [
    path('', HomeView.as_view(),),
    path('register/', RegisterView.as_view(),name='register',),
    path('login/', CustomLoginView.as_view(),name='login',),
    path('logout/', CustomLogoutView.as_view(),name='logout',),
    path('dashboard/', DashboardView.as_view(),name='dashboard',),
    path('add/', AddStockView.as_view(),name='add_stock',),
    path('update/<int:pk>/', UpdateStockView.as_view(),name='update_stock',),
    path('delete/<int:pk>/', DeleteStockView.as_view(),name='delete_stock',),
]
