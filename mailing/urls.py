from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (
    MailingCreateView, MailingListView, MailingDeleteView, MailingUpdateView, ClientListView, ClientCreateView,
    ClientUpdateView, ClientDeleteView
)

app_name = MailingConfig.name

urlpatterns = [
    # path('client_create/', ClientCreateView.as_view(), name='client_create'),
    # path('', ClientListView.as_view(), name='client_list'),
    # path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    # path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('', MailingListView.as_view(), name='mailing_list'),
    # path('mailing_view/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    # path('mailing_edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
]