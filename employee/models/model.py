from django.db import models
from employers.models.models import Employers



class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    salary = models.PositiveIntegerField(default=0)
    profession = models.TextField(blank=True)
    employer = models.ForeignKey(Employers, on_delete=models.CASCADE)    
    
    
    def __str__(self):
        return self.name