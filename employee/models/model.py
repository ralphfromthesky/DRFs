from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    salary = models.PositiveIntegerField(default=0)
    profession = models.TextField(blank=True)

    def __str__(self):
        return self.name