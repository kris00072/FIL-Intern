from django.db import models
from model_app.models import CommonInfo
class Employee(CommonInfo):
    managed_by = models.CharField(max_length=100,default='None')



    def __str__(self):
        return self.first_name
