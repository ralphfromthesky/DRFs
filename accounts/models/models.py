from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    full_name = models.CharField(max_length=100, blank=True, default='')
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(blank=True, default='')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, default='')

    def __str__(self):
        return f"{self.user.username} - {self.role}"