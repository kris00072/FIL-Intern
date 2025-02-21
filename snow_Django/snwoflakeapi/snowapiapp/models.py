from django.db import models

class Trip(models.Model):
    trip_id = models.BigAutoField(primary_key=True)
    trip_name = models.CharField(max_length=255, blank=True, null=True)
    trip_duration = models.CharField(max_length=100, blank=True, null=True)
    start_location = models.CharField(max_length=255, blank=True, null=True)
    end_location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    trip_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    def __str__(self):
        return self.trip_name if self.trip_name else f"Trip {self.trip_id}"
