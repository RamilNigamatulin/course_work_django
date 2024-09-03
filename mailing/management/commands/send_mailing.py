from django.core.management.base import BaseCommand
from mailing.services import send_mailing

class Command(BaseCommand):
    help = 'Send mailings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Sending mailings...')
        send_mailing()
        self.stdout.write(self.style.SUCCESS('Mailings sent successfully.'))