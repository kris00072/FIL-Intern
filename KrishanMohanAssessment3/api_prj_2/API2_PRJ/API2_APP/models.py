from django.db import models

class API2(models.Model):
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.pincode} - Price: {self.state}"
