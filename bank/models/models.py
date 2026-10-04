from django.db import models
from employers.models.models import Employers
class Banks(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    gross_amount = models.DecimalField(max_digits=12, decimal_places=2)    
    employer = models.ForeignKey(Employers, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.bank_name