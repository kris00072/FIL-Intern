from django.contrib import admin
from .models import API2

@admin.register(API2)
class API2Admin(admin.ModelAdmin):
    list_display = ('pincode', 'state', 'district')  
    search_fields = ('pincode', 'state', 'district')  
    list_filter = ('state', 'district')  
