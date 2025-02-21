from django.contrib import admin
from .models import API1

@admin.register(API1)
class API1Admin(admin.ModelAdmin):
    list_display = ('item_id', 'item', 'price')  
    search_fields = ('item',)  
    list_filter = ('price',)  
