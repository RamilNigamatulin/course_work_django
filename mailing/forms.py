from django.forms import ModelForm, BooleanField
from mailing.models import Message, Mailing, Client, Attempt
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        # fields = ('letter_subject', 'text_letter', 'owner')


class MessageModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        # fields = ('letter_subject', 'text_letter', 'owner')


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
        # fields = ('periodicity', 'status', 'owner')


class MailingModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
        # fields = ('periodicity', 'status', 'owner')


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

