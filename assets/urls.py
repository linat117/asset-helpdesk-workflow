from rest_framework.routers import DefaultRouter 
from .views import AssetViewSet, AssignmentViewSet, MaintenanceLogViewSet
from django.urls import path
from .views import (AssetCreateView, AssetDeleteView,AssetDetailView, AssetListView, AssetUpdateView,
                    AssignmentCreateView, AssignmentDeleteView, AssignmentDetailView, AssignmentListView, AssignmentUpdateView,
                    MaintenanceLogCreateView, MaintenanceLogDeleteView, MaintenanceLogDetailView, MaintenanceLogListView, MaintenanceLogUpdateView)
    
urlpatterns = [
    path('assets/', AssetListView.as_view(), name= 'asset-list' ),
    path('assets/create/', AssetCreateView.as_view(), name= 'asset-add'),
    path('assets/<int:pk>/update/', AssetUpdateView.as_view(), name= 'asste-update'),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view(), name= 'asset-delete'),
    path('assets/<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),

    path('assignments/', AssignmentListView.as_view(), name= 'assignment-list' ),
    path('assignment/create/', AssignmentCreateView.as_view(), name= 'assignment-add'),
    path('assignment/<int:pk>/update/', AssignmentUpdateView.as_view(), name= 'assignment-update'),
    path('assignment/<int:pk>/delete/', AssignmentDeleteView.as_view(), name= 'assignment-delete'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),

    path('maintenancelogs/', MaintenanceLogListView.as_view(), name= 'maintenancelog-list' ),
    path('maintenancelog/create/', MaintenanceLogCreateView.as_view(), name= 'maintenancelog-add'),
    path('maintenancelog/<int:pk>/update/', MaintenanceLogUpdateView.as_view(), name= 'maintenancelog-update'),
    path('maintenancelog/<int:pk>/delete/', MaintenanceLogDeleteView.as_view(), name= 'maintenancelog-delete'),
    path('maintenancelog/<int:pk>/', MaintenanceLogDetailView.as_view(), name='maintenancelog-detail'),

]
#url for DRF
router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'maintenancelogs', MaintenanceLogViewSet)

urlpatterns = router.urls