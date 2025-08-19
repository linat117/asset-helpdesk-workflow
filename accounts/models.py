from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ROLE_CHOICE = [
        ('admin', 'Admin'),
        ('it_head', 'IT Head'),
        ('it_staff', 'IT Staff'),
        ('employee', 'Employee')
    ]
    role = models.CharField(max_length= 50, choices=ROLE_CHOICE, default='employee')

    def __str__(self):
        return f"{self.username} - {self.role}"