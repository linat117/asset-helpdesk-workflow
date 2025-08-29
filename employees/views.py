from rest_framework import viewsets 
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import EmployeePermission, DepartmentPermission,IsAdminOnly
from rest_framework.response import Response
from rest_framework import status
#employee views
"""class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee 
    template_name = 'employees/employee_delete_confirm.html'
    success_url = reverse_lazy('employee-list')

#department views
class DepartmentListView(ListView):
    model = Employee
    template_name = 'departments/department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Employee
    template_name = 'departments/department_detail.html'
    context_object_name = 'department'

class DepartmentCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('department-list')
    permission_classes = [IsAuthenticated, IsAdminOnly]
    

class DepartmentUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('depatment-list')
    
class DepartmentDeleteView(DeleteView):
    model = Employee 
    template_name = 'departments/department_delete_confirm.html'
    success_url = reverse_lazy('department-list') 
    """
#employee viewset for drf
class EmployeeViewSet(viewsets.ModelViewSet):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return Employee.objects.all()
        elif user.role == 'it_staff':
            # IT Staff should NOT see all employees - they should only see their own
            try:
                return Employee.objects.filter(user=user)
            except:
                return Employee.objects.filter(email=user.email)
        elif user.role == 'it_head':
            # IT Head should NOT see all employees - they should only see their own
            try:
                return Employee.objects.filter(user=user)
            except:
                return Employee.objects.filter(email=user.email)
        elif user.role == 'employee':
            # Employees can only see their own record
            try:
                return Employee.objects.filter(user=user)
            except:
                return Employee.objects.filter(email=user.email)
        
        return Employee.objects.none()
    
    def list(self, request, *args, **kwargs):
        # For employees, return single record instead of list
        if request.user.role == 'employee':
            queryset = self.get_queryset()
            if queryset.exists():
                serializer = self.get_serializer(queryset.first())
                return Response(serializer.data)
            else:
                return Response({"error": "Employee record not found"}, status=404)
        
        return super().list(request, *args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                employee = serializer.save()
                
                # Check if user account was created
                username = request.data.get('username')
                password = request.data.get('password')
                
                if username and password:
                    return Response({
                        "message": "Employee and user account created successfully",
                        "employee": {
                            "id": employee.id,
                            "first_name": employee.first_name,
                            "last_name": employee.last_name,
                            "email": employee.email,
                            "position": employee.position,
                            "role": employee.role,
                            "department": employee.department.id
                        },
                        "user_account": {
                            "username": username,
                            "email": employee.email,
                            "role": employee.role,
                            "login_ready": True
                        },
                        "instructions": "Employee can now login using the provided username and password"
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "message": "Employee created successfully (no user account)",
                        "employee": EmployeeSerializer(employee).data,
                        "user_account": None,
                        "note": "User account not created. Employee cannot login until user account is created separately."
                    }, status=status.HTTP_201_CREATED)
                    
            except Exception as e:
                return Response({
                    "error": "Failed to create employee",
                    "detail": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "error": "Invalid data",
            "details": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
#department viewset for drf
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]