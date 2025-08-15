from rest_framework import viewsets 
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

#employee views
class EmployeeListView(ListView):
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
    template_name = 'employees/employee_delete_confirm'
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

class DepartmentUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'departments/department_form.html'
    success_url = reverse_lazy('depatment-list')

class DepartmentDeleteView(DeleteView):
    model = Employee 
    template_name = 'departments/department_delete_confirm'
    success_url = reverse_lazy('department-list') 
#employee viewset for drf
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#employee viewset for drf
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer