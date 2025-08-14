from django.urls import path
from .views import EmployeeCreateView, EmployeeDeleteView, EmployeeDetailView, EmployeeListView, EmployeeUpdateView
urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name= 'employee-list' ),
    path('employee/create/', EmployeeCreateView.as_view(), name= 'employee-add'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name= 'employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name= 'employee-delete'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]