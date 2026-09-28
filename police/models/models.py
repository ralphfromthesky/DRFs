from django.db import models

class Police(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    isWorking = models.BooleanField(default=True)
    salary = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.name