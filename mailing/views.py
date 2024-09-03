from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse

from mailing.forms import (MessageForm, MessageModeratorForm, MailingModeratorForm, MailingForm,
                           ClientForm, ClientModeratorForm)

from mailing.models import Mailing, Client, Message, Attempt
from blog.models import Blog

from django.core.management import call_command
from django.http import HttpResponse


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.status = 'created'
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingModeratorForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.status = 'updated'
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name ='mailing/mailing_detail.html'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingForm
        if user.has_perm('mailing.can_view_mailing'):
            return MailingModeratorForm
        raise PermissionDenied


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientModeratorForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailing/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:client_list')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_blogs'] = Blog.objects.order_by('?')[:3]
        return context


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


class AttemptListView(ListView):
    model = Attempt
    template_name = 'mailing/attempt_list.html'
    context_object_name = 'attempts'


class HomeView(TemplateView):
    template_name = 'mailing/home_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='launched').count()
        context['unique_clients'] = Client.objects.values('contact_email').distinct().count()
        context['random_blogs'] = Blog.objects.order_by('?')[:3]
        return context
