from django.contrib import admin
from .models import Asset, Assignment, MaintenanceLog

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'serial_number', 'status', 'purchase_date')
    list_filter = ('status', 'category', 'purchase_date')
    search_fields = ('name', 'serial_number', 'category')
    ordering = ('name',)
    date_hierarchy = 'purchase_date'

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'assigned_date', 'return_date')
    list_filter = ('assigned_date', 'return_date', 'asset__category')
    search_fields = ('asset__name', 'employee__first_name', 'employee__last_name')
    ordering = ('-assigned_date',)
    date_hierarchy = 'assigned_date'
    raw_id_fields = ('asset', 'employee')

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('asset', 'maintenance_type', 'technician', 'performed_by', 'maintenance_date', 'cost')
    list_filter = ('maintenance_type', 'maintenance_date', 'asset__category')
    search_fields = ('asset__name', 'technician', 'description')
    ordering = ('-maintenance_date',)
    date_hierarchy = 'maintenance_date'
    raw_id_fields = ('asset', 'performed_by')
    list_per_page = 20