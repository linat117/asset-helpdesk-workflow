from django.db import models
from employees.models import Employee
from assets.models import Asset

class TicketCategory(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Ticket(models.Model):

    TICKET_STATUS = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
     ]
    
    TICKET_PRIORITY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ]

    title = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE, related_name='tickets')
    status = models.CharField(choices = TICKET_STATUS, max_length = 100)
    priority = models.CharField(choices= TICKET_PRIORITY, max_length=100)
    reported_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tickets')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_tickets', null=True)
    linked_asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name = 'tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}({self.status} reported by :{self.reported_by} for the asset : {self.linked_asset})"

class TicketUpdateLog(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE, related_name = 'ticketupdatelogs')
    updated_by= models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ticketupdatelogs')
    update_note=  models.TextField()
    update_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.ticket} updated by {self.updated_by}"
    

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticketcomments')
    commenter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ticketcomments')
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.comment_text}
