from django.db import models
from django.core.validators import MaxValueValidator

class Gamers(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(99)])
    address = models.CharField(max_length=100)
    isPlaying = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name