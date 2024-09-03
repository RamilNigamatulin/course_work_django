from django.contrib import admin
from mailing.models import Client, Mailing, Message, Attempt

admin.site.register(Client)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_email', 'surname', 'name', 'patronimic', 'comment',)
    list_filter = ('contact_email', 'surname', 'name',)
    search_fields = ('contact_email', 'surname', 'name',)


admin.site.register(Mailing)


class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'periodicity', 'status',)
    list_filter = ('start_date', 'periodicity', 'status',)
    search_fields = ('start_date', 'periodicity', 'status',)


admin.site.register(Message)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'letter_subject', 'text_letter', 'message', 'clients',)
    list_filter = ('letter_subject', 'text_letter', 'message', 'clients',)
    search_fields = ('letter_subject', 'text_letter', 'message', 'clients',)


admin.site.register(Attempt)


class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing', 'attempt_time', 'status', 'server_response',)
    list_filter = ('mailing', 'attempt_time', 'status', 'server_response',)
    search_fields = ('mailing', 'attempt_time', 'status', 'server_response',)

# Register your models here.
