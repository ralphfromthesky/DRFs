from django.db import models

class Employers(models.Model):
    owner = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    is_stable = models.BooleanField(default=True)
    office_address = models.CharField(max_length=100)
    profit = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.company_name