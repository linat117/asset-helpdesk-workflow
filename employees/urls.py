from rest_framework.routers import DefaultRouter 
from .views import EmployeeViewSet, DepartmentViewSet
from django.urls import path
#from .views import (EmployeeCreateView, EmployeeDeleteView, EmployeeDetailView, EmployeeListView, EmployeeUpdateView  , DepartmentCreateView, DepartmentDeleteView, DepartmentDetailView, DepartmentListView, DepartmentUpdateView)
#url for DRF
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename = 'employee')
router.register(r'departments', DepartmentViewSet)
""" urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name= 'employee-list' ),
    path('employee/create/', EmployeeCreateView.as_view(), name= 'employee-add'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name= 'employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name= 'employee-delete'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('departments/', DepartmentListView.as_view(), name= 'department-list' ),
    path('department/create/', DepartmentCreateView.as_view(), name= 'department-add'),
    path('department/<int:pk>/update/', DepartmentUpdateView.as_view(), name= 'department-update'),
    path('department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name= 'department-delete'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]"""

urlpatterns = router.urls