from django.contrib import admin
from .models import Employee, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'role', 'department', 'user')
    list_filter = ('role', 'department', 'position')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    ordering = ('first_name', 'last_name')
    raw_id_fields = ('user', 'department')