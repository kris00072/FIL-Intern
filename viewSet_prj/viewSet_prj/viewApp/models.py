from django.db import models

class BlackHoles(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    mass = models.CharField(max_length=100)

    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

