from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy, reverse

from mailing.forms import (MessageForm, MessageModeratorForm, MailingModeratorForm, MailingForm,
                           ClientForm, ClientModeratorForm)

from mailing.models import Mailing, Client, Message, Attempt
from blog.models import Blog

from django.core.management import call_command
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect



class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.status = 'created'
        mailing = form.save(commit=False)
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.groups.filter(name='manager').exists():
            return queryset
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingModeratorForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.status = 'updated'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailing:mailing_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user == self.object.owner:
            return MailingForm
        elif user.has_perm('mailing.can_disable_mailings'):
            return MailingModeratorForm
        else:
            raise PermissionDenied


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or user == self.object.owner or user.groups.filter(name='manager').exists():
            return self.object
        else:
            raise PermissionDenied


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.groups.filter(name='manager').exists():
            return queryset
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save(commit=False)
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientModeratorForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')

    def get_success_url(self):
        return reverse('mailing:client_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'mailing/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save(commit=False)
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_blogs'] = Blog.objects.order_by('?')[:3]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageModeratorForm
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy('mailing:message_list')

    def get_success_url(self):
        return reverse('mailing:message_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mailing/message_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser or self.request.user == self.object.owner:
            return self.object
        else:
            raise PermissionDenied


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    template_name = 'mailing/attempt_list.html'
    context_object_name = 'attempts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        if self.request.user.is_authenticated:
            queryset = queryset.filter(mailing__owner=self.request.user)
        return queryset


class HomeView(TemplateView):
    template_name = 'mailing/home_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='launched').count()
        context['unique_clients'] = Client.objects.values('contact_email').distinct().count()
        context['random_blogs'] = Blog.objects.order_by('?')[:3]
        return context
