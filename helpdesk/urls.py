from rest_framework.routers import DefaultRouter 
from .views import (TicketViewSet, TicketCommentViewSet, TicketUpdateLogViewSet, TicketCategoryViewSet,
                    TicketCategoryCreateView, TicketCategoryDeleteView, TicketCategoryDetailView, TicketCategoryListView, TicketCategoryUpdateView,
                    TicketCommentCreateView, TicketCommentDeleteView, TicketCommentDetailView, TicketCommentListView, TicketCommentUpdateView,
                    TicketUpdateLogUpdateView, TicketUpdateLogCreateView, TicketUpdateLogDeleteView, TicketUpdateLogDetailView, TicketUpdateLogListView
                    ,TicketListView, TicketCreateView, TicketDeleteView, TicketDetailView, TicketUpdateView)
from django.urls import path 

#url for DRF 
router = DefaultRouter() 
router.register(r'tickets', TicketViewSet)
router.register(r'ticketcomments',TicketCommentViewSet)
router.register(r'ticketupdatelogs', TicketUpdateLogViewSet)
router.register(r'ticketcategories', TicketCategoryViewSet)
urlpatterns = router.urls
"""
urlpatterns = [
    #ticket urls
    path('tickets/', TicketListView.as_view(), name= 'ticket-list' ),
    path('ticket/create/', TicketCreateView.as_view(), name= 'ticket-add'),
    path('ticket/<int:pk>/update/', TicketUpdateView.as_view(), name= 'ticket-update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name= 'ticket-delete'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    #ticket category urls
    path('ticketcategories/', TicketCategoryListView.as_view(), name= 'ticket-category-list' ),
    path('ticketcategory/create/', TicketCategoryCreateView.as_view(), name= 'ticket-category-add'),
    path('ticketcategory/<int:pk>/update/', TicketCategoryUpdateView.as_view(), name= 'ticket-category-update'),
    path('ticketcategory/<int:pk>/delete/', TicketCategoryDeleteView.as_view(), name= 'ticket-category-delete'),
    path('ticketcategory/<int:pk>/', TicketCategoryDetailView.as_view(), name='ticket-category-detail'),
#ticket upate log urls 
    path('ticketupdatelogs/', TicketUpdateLogListView.as_view(), name= 'ticketupdatelog-list' ),
    path('ticketupdatelog/create/', TicketUpdateLogCreateView.as_view(), name= 'ticketupdatelog-add'),
    path('ticketupdatelog/<int:pk>/update/', TicketUpdateLogUpdateView.as_view(), name= 'ticketupdatelog-update'),
    path('ticketupdatelog/<int:pk>/delete/', TicketUpdateLogDeleteView.as_view(), name= 'ticketupdatelog-delete'),
    path('ticketupdatelog/<int:pk>/', TicketUpdateLogDetailView.as_view(), name='ticketupdatelog-detail'),
# ticket comment urls
    path('ticketcomments/', TicketCommentListView.as_view(), name= 'ticketcomment-list' ),
    path('ticketcomment/create/', TicketCommentCreateView.as_view(), name= 'ticketcomment-add'),
    path('ticketcomment/<int:pk>/update/', TicketCommentUpdateView.as_view(), name= 'ticketcomment-update'),
    path('ticketcomment/<int:pk>/delete/', TicketCommentDeleteView.as_view(), name= 'ticketcomment-delete'),
    path('ticketcomment/<int:pk>/', TicketCommentDetailView.as_view(), name='ticketcomment-detail'),

]
"""
