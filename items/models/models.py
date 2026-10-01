from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_count = models.PositiveIntegerField(default=0)
    item_descriptions = models.CharField(default=100)
    is_available = models.BooleanField(default=True)
    value = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.item_name