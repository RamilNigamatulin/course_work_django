from django.forms import ModelForm
from mailing.models import Message, Mailing, Client, Attempt
from django import forms


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('letter_subject', 'text_letter',)


class MessageModeratorForm(ModelForm):
    class Meta:
        model = Message
        fields = ('letter_subject', 'text_letter',)


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingModeratorForm(ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientModeratorForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields = '__all__'


class AttemptModeratorForm(ModelForm):
    class Meta:
        model = Attempt
        fields = '__all__'

