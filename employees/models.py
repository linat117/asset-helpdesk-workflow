from django.db import models


class Department(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    
    #POSITION_CHOICES = [
     #   ('it_technician', 'It Technician'),
     #   ('finance_manager', 'Finance Manager'),
    #    ('customer_service', 'Customer Service'),
    #]
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('it_head', 'IT Head'),
        ('it_staff', 'IT Staff'),
        ('employee', 'Employee'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length = 150)
    #position = models.CharField(choices= POSITION_CHOICES, max_length=20)
    position = models.CharField( max_length=191)
    role = models.CharField(choices=ROLE_CHOICES, max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role}) - {self.position} from {self.department} department"