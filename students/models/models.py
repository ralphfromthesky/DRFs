from django.db import models


class Students(models.Model):
        full_name = models.CharField(max_length=100)      
        address = models.TextField(blank=True)
        course = models.TextField(blank=True)
        isStudy = models.BooleanField(default=True)
        
        def __str__(self):
            return self.full_name