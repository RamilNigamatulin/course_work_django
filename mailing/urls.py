from django.urls import path
from mailing.apps import MailingConfig
from mailing.models import Message, Mailing, Attempt, Client
from mailing.views import (MailingCreateView, MailingListView, MailingDeleteView, MailingUpdateView, MailingDetailView,
                           ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView,
                           MessageListView, MessageDetailView, MessageCreateView, MessageDeleteView, MessageUpdateView,
                           AttemptListView, HomeView
)


app_name = MailingConfig.name


urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_confirm_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_confirm_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_confirm_delete'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),

    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_confirm_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_confirm_delete'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),

    path('attempts/', AttemptListView.as_view(), name='attempt_list'),
]
