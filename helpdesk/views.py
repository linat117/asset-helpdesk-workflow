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

