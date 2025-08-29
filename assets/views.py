from  django.views.generic import ListView,  DetailView, DeleteView, UpdateView, CreateView
from .models import Asset, Assignment, MaintenanceLog
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import AssetPermission, AssignmentPermission, MaintenanceLogPermission,IsAdminOnly, IsAdminOrITStaff
from .serializers import AssetSerializer, AssignmentSerializer , MaintenanceLogSerializer
# views for Asset model
class AssetListView(ListView):
    model = Asset
    template_name = 'assets/asset_list.html'
    context_object_name = 'assets'

class AssetDetailView(DetailView):
    model = Asset
    template_name = 'assets/asset_detail.html'
    context_object_name = 'asset'

class AssetCreateView(CreateView):
    model = Asset
    fields = '__all__'
    template_name = 'assets/asset_form.html'
    success_url = reverse_lazy('asset-list')

class AssetUpdateView(UpdateView):
    model = Asset
    fields = '__all__'
    template_name = 'assets/asset_form.html'
    success_url = reverse_lazy('asset-list')

class AssetDeleteView(DeleteView):
    model = Asset 
    template_name = 'assets/asset_delete_confirm.html'
    success_url = reverse_lazy('asset-list')

#views for assignment model
class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignments/assignment_list.html'
    context_object_name = 'assignments'

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignments/assignment_detail.html'
    context_object_name = 'assignment'

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = '__all__'
    template_name = 'assignments/assignment_form.html'
    success_url = reverse_lazy('assignment-list')

class AssignmentUpdateView(UpdateView):
    model = Assignment
    fields = '__all__'
    template_name = 'assignments/assignment_form.html'
    success_url = reverse_lazy('assignment-list')

class AssignmentDeleteView(DeleteView):
    model = Assignment 
    template_name = 'assignments/assignment_delete_confirm.html'
    success_url = reverse_lazy('assignment-list')

#views for maintenance log models
class MaintenanceLogListView(ListView):
    model = MaintenanceLog
    template_name = 'maintenancelogs/maintenancelog_list.html'
    context_object_name = 'maintenancelogs'

class MaintenanceLogDetailView(DetailView):
    model = MaintenanceLog
    template_name = 'maintenancelogs/maintenancelog_detail.html'
    context_object_name = 'maintenancelog'

class MaintenanceLogCreateView(CreateView):
    model =MaintenanceLog
    fields = '__all__'
    template_name = 'maintenancelogs/maintenancelog_form.html'
    success_url = reverse_lazy('maintenancelog-list')

class MaintenanceLogUpdateView(UpdateView):
    model = MaintenanceLog
    fields = '__all__'
    template_name = 'maintenancelogs/maintenancelog_form.html'
    success_url = reverse_lazy('maintenancelog-list')

class MaintenanceLogDeleteView(DeleteView):
    model = MaintenanceLog
    template_name = 'maintenancelogs/maintenancelog_delete_confirm.html'
    success_url = reverse_lazy('maintenancelog-list')


#Asset views set for drf

class AssetViewSet(viewsets.ModelViewSet):
    #queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminOrITStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return Asset.objects.all()
        elif user.role == 'it_staff':
            return Asset.objects.all()
        elif user.role == 'employee':
            
             return Asset.objects.filter(assignments__employee__user=user)
        
        return Asset.objects.none()
#Maintenancelog view set for drf
class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [IsAuthenticated, IsAdminOrITStaff]

#Assignments view set for drf
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, AssignmentPermission]
    
   
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminOnly]  # Only admin can create/update/delete
        else:
            permission_classes = [IsAuthenticated]  # All authenticated users can read
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return Assignment.objects.all()
        elif user.role == 'it_head':
            return Assignment.objects.all()
        elif user.role == 'it_staff':
            # IT Staff can only see assignments assigned to themselves
            try:
                return Assignment.objects.filter(employee__user=user)
            except:
                # Fallback if no user relationship
                return Assignment.objects.filter(employee__email=user.email)
        elif user.role == 'employee':
            # Employees can only see assignments assigned to themselves
            try:
                return Assignment.objects.filter(employee__user=user)
            except:
                return Assignment.objects.filter(employee__email=user.email)
        
        return Assignment.objects.none()




