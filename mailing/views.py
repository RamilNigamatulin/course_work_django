from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from mailing.models import Mailing, Client, Message


class MailingCreateView(CreateView):
    model = Mailing
    template_name = 'mailing_views.html'
    success_url = '/mailing/'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_views.html'



class MailingDeleteView(DeleteView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing


class ClientListView(ListView):
    model = Client
    template_name = 'client_views.html'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_create.html'
    success_url = '/mailing/'


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    success_url = '/clients/'


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = '/clients/'

# Create your views here.