from django.db import models

class API1(models.Model):
    item_id = models.IntegerField(primary_key=True)  
    item = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.item} - Price: {self.price}"

