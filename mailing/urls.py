from django.urls import path
from mailing.apps import MailingConfig
from mailing.models import Message, Mailing, Attempt, Client
from mailing.views import (
    MailingCreateView, MailingListView, MailingDeleteView, MailingUpdateView, MailingDetailView,
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView,
    MessageListView, MessageDetailView, MessageCreateView, MessageDeleteView, MessageUpdateView,
)

app_name = MailingConfig.name

urlpatterns = [
    # path('client_create/', ClientCreateView.as_view(), name='client_create'),
    # path('', ClientListView.as_view(), name='client_list'),
    # path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    # path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    # path('', MailingListView.as_view(), name='mailing_list'),
    # path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    # path('mailing_view/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    # path('mailing_edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),

    path('', MessageListView.as_view(), name='message_list'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_confirm_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),

]