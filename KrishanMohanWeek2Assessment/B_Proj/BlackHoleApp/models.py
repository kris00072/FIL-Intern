from django.db import models

class BlackHole(models.Model):
    Bid = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=100)
    mass = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    event_horizon = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
