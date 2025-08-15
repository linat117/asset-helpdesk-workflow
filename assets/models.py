from django.db import models
from ..employees.models import Employee
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
    serial_number = models.CharField(max_length= 200, unique= True)
    purchase_date = models.DateField()
    status = models.CharField(choices= STATUS_CHOICES, max_length = 100)


class Assignment(models.Model):
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='assignments')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignments')
    assigned_date = models.DateField()
    return_date = models.DateField()

class MaintenanceLog(models.Model):
    asset_id = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='maintenancelogs')
    description = models.TextField()
    date = models.DateField()
    performed_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='maintenancelogs')