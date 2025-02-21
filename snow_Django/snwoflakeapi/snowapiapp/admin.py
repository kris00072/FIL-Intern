from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'trip_name', 'start_location', 'end_location', 'start_date', 'end_date', 'trip_cost')
    search_fields = ('trip_name', 'start_location', 'end_location')
    list_filter = ('start_date', 'end_date')
    ordering = ('start_date',)

# Alternative way to register (without @admin.register decorator)
# admin.site.register(Trip, TripAdmin)
