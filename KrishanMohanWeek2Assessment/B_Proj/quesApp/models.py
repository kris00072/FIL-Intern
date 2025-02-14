from django.db import models

class Questions(models.Model):
    qno = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100)
    question = models.TextField()
