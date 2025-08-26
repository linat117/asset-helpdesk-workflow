from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsITHead(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'it_head'

# Admin only
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'


# Admin or IT Staff full access
class IsAdminOrITStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['Admin', 'IT Staff']


# Admin full CRUD, IT Staff read/update, others read-only
class AssetPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.role == 'admin':
            return True 
        elif request.user.role == 'IT Staff':
            
            return request.method in SAFE_METHODS + ('PUT', 'PATCH')
        else:
            
            return request.method in SAFE_METHODS


# Maintenance log permission
class MaintenanceLogPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.role in ['admin', 'it_staff']:
            return True  
        else:
            return request.method in SAFE_METHODS 


# Assignment permission
class AssignmentPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.role in ['admin', 'IT Staff']:
            return True  
        else:
            return request.method in SAFE_METHODS 


# Employee permissions
class EmployeePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Admin full CRUD
        if request.user.role == 'admin':
            return True
        
        # IT Staff can read and update employees
        elif request.user.role == 'it_staff':
            return request.method in SAFE_METHODS + ('PUT', 'PATCH')
        
        # Employees can only view their own details
        elif request.user.role == 'employee':
            return request.method in SAFE_METHODS
        
        return False


# Department permissions
class DepartmentPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Admin full CRUD
        if request.user.role == 'admin':
            return True
        
        # IT Head can also manage departments
        elif request.user.role == 'it_head':
            return True
        
        # Others can only read department data
        else:
            return request.method in SAFE_METHODS

#ticket permissions
class TicketPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.role == 'admin':
            return True 
        elif request.user.role == 'it_staff':
            
            return request.method in SAFE_METHODS + ('PUT', 'PATCH')
        else:
            
            return request.method in SAFE_METHODS
