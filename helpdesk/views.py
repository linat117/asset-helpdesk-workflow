from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import TicketCategorySerializer, TicketCommentSerializer, TicketSerializer, TicketUpdateLogSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Ticket, TicketCategory, TicketComment, TicketUpdateLog
#ticket category crud views
class TicketCategoryListView(ListView):
    model = TicketCategory
    template_name = 'ticketcategories/ticketcategory_list.html'
    context_object_name = 'ticketcategories'

class TicketCategoryDetailView(DetailView):
    model = TicketCategory
    template_name = 'ticketcategories/ticketcategory_detail.html'
    context_object_name = 'ticketcategory'

class TicketCategoryCreateView(CreateView):
    model = TicketCategory
    fields = '__all__'
    template_name = 'ticketcategories/ticketcategory_form.html'
    success_url = reverse_lazy('ticket-category-list')

class TicketCategoryUpdateView(UpdateView):
    model = TicketCategory
    fields = '__all__'
    template_name= 'ticketcategories/tickecategory_form.html'
    success_url = reverse_lazy('ticket-category-list')

class TicketCategoryDeleteView(DeleteView):
    model = TicketCategory
    template_name = 'ticketcategories/ticketcategory_delete_confirm.html'
    success_url = reverse_lazy('ticket-category-list')

# viewset for  the serializer for drf 

class TicketCategoryViewSet(viewsets.ModelViewSet):
    queryset = TicketCategory.objects.all() 
    serializer_class = TicketCategorySerializer


#view for Ticket Model 
class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name ='tickets'

class TicketDetailView(DetailView):
    model = Ticket 
    template_name = 'tickets/ticket_detail.html'
    context_object_name ='ticket'

class TicketCreateView(CreateView):
    model = Ticket
    fields ='__all__'
    template_name = 'tickets/ticket_form.html'
    success_url = 'ticket-list'

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = '__all__'
    template_name = 'tickets/ticket_form.html'
    success_url = 'ticket-list'

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = 'ticket-list'

#viewset for ticketserializer for DRF
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


#view for ticket update logs
class TicketUpdateLogListView(ListView):
    model = TicketUpdateLog 
    template_name = 'ticketupdatelogs/ticketupdatelog_list.html'
    context_object_name = 'ticketupdatelogs'

class TicketUpdateLogDetailView(DetailView):
    model = TicketUpdateLog
    template_name = 'ticketupdatelogs/ticketupdatelogs_detail.html'
    context_object_name = 'ticketupdatelog'

class TicketUpdateLogCreateView(CreateView):
    model = TicketUpdateLog
    fields = '__all__'
    template_name = 'ticketupdatelogs/ticketupdatelogs_form.html'
    success_url = 'ticketupdatelog-list'

class TicketUpateLogUpdateView(UpdateView):
    model = TicketUpdateLog
    fields = '__all__'
    template_name = 'ticketupdatelogs/ticketupdatelogs_form.html'
    success_url = 'ticketupdatelog-list'

class TicketUpdateLogDeleteView(DeleteView):
    model = TicketUpdateLog
    template_name = 'ticketupdatelogs/ticketupdatelogs_delete_confirm.html'
    success_url = 'ticketupdatelog-list'

#viewset for ticketupdatelog serializer for drf

class TicketUpdateLogViewSet(viewsets.ModelViewSet):
    queryset = TicketUpdateLog.objects.all()
    serializer_class = TicketUpdateLogSerializer 


#view for ticket comment 
class TicketCommentListView(ListView):
    model  = TicketComment 
    template_name = 'ticketcomments/ticketcomment_list.html'
    context_object_name = 'ticketcomments'

class TicketCommentDetailView(DetailView):
    model = TicketComment 
    template_name = 'ticketcomments/ticketcomment_detail.html'
    context_object_name = 'ticketcomment'

class TicketCommentCreateView(CreateView):
    model = TicketComment 
    template_name = 'ticketcomments/ticketcomment_form.html'
    fields = '__all__'
    success_url = 'ticketcomment-list'

class TicketCommentUpdateView(UpdateView):
    model = TicketComment 
    template_name = 'ticketcomments/ticketcomment_form.html'
    fields = '__all__'
    success_url = 'ticketcomment-list'

class TicketCommentDeleteView(DeleteView):
    model = TicketComment 
    fields = '__all__'
    template_name = 'ticketcomments/ticketcomment_confirm_delete.html'
    success_url = 'ticketcomment-list'

#viewset for Ticket comment serializer

class TicketCommentViewSet(viewsets.ModelViewSet):
    queryset = TicketComment.objects.all() 
    serializer_class = TicketCommentSerializer