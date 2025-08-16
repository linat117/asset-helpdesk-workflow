from django.db import models
from employees.models import Employee
# Create your models here.
class Asset(models.Model):
    STATUS_CHOICES = [
        ('active' , 'Active'),
        ('in_maintenance','In Maintenance'),
        ('retired', 'Retired'),
        ('lost', 'Lost'),
        ('disposed','Disposed'),
    ]

    name = models.CharField(max_length = 100)
    category = models.CharField(max_length=100)
    serial_number = models.CharField(max_length= 191, unique= True)
    purchase_date = models.DateField()
    status = models.CharField(choices= STATUS_CHOICES, max_length = 100)
    
    def __str__(self):
        return f"{self.name}({self.category}) : {self.status}"

class Assignment(models.Model):
    asset= models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assignments')
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignments')
    assigned_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self):
        return f"{self.asset} assigned to {self.employee}"

class MaintenanceLog(models.Model):
    asset= models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='maintenancelogs')
    description = models.TextField()
    date = models.DateField()
    performed_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='maintenancelogs')

    def __str__(self):
        return f"{self.asset} maintained by {self.performed_by}."