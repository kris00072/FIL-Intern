from django.db import models

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_id = models.IntegerField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_joining = models.DateField()

    class Meta:
        abstract = True 

class Manager(CommonInfo): 
    manages = models.IntegerField()  
