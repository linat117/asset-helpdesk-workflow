from rest_framework.routers import DefaultRouter 
from .views import (TicketViewSet, TicketCommentViewSet, TicketUpdateLogViewSet, TicketCategoryViewSet,
                    TicketCategoryCreateView, TicketCategoryDeleteView, TicketCategoryDetailView, TicketCategoryListView, TicketCategoryUpdateView,
                    TicketCommentCreateView, TicketCommentDeleteView, TicketCommentDetailView, TicketCommentListView, TicketCommentUpdateView,
                    TicketUpateLogUpdateView, TicketUpdateLogCreateView, TicketUpdateLogDeleteView, TicketUpdateLogDetailView, TicketUpdateLogListView
                    ,TicketListView, TicketCreateView, TicketDeleteView, TicketDetailView, TicketUpdateView)
from django.urls import path 

#url for DRF 
router = DefaultRouter() 
router.register(r'tickets', TicketViewSet)
router.register(r'ticketcomments',TicketCommentViewSet)
router.register(r'ticketupdatelogs', TicketUpdateLogViewSet)
router.register(r'ticketcategories', TicketCategoryViewSet)
urlpatterns = router.urls
urlpatterns = [
    path('tickets/', TicketListView.as_view(), name= 'ticket-list' ),
    path('ticket/create/', TicketCreateView.as_view(), name= 'ticket-add'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name= 'ticket-update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name= 'ticket-delete'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),

    

]