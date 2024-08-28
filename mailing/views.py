from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from mailing.forms import (MessageForm, MessageModeratorForm, MailingModeratorForm, MailingForm,
                           ClientForm, ClientModeratorForm, AttemptForm, AttemptModeratorForm)
from mailing.models import Mailing, Client, Message


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_views.html'
    success_url = reverse_lazy('mailing:message_list')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_views.html'


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingModeratorForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('mailing:message_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name ='message_detail.html'


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_views.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_create.html'
    success_url = reverse_lazy('mailing:message_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientModeratorForm
    template_name = 'mailing/client_update.html'
    success_url = reverse_lazy('mailing:message_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailing/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageModeratorForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message
    template_name ='mailing/message_detail.html'

# Create your views here.