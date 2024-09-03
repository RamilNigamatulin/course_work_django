from datetime import datetime
import pytz
from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Attempt, Message
import smtplib
import logging


logger = logging.getLogger(__name__)


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(
        status='launched'
    )

    for mailing in mailings:
        try:
            message = Message.objects.get(mailing=mailing)
        except Message.DoesNotExist:
            logger.warning(f'No message found for mailing {mailing.id}')
            continue

        for client in mailing.clients.all():
            try:
                response = send_mail(
                    subject=message.letter_subject,
                    message=message.text_letter,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.contact_email],
                    fail_silently=False
                )
                Attempt.objects.create(
                    mailing=mailing,
                    status='success',
                    server_response=str(response)
                )
                logger.info(f'Successfully sent mailing to {client.contact_email}')
            except smtplib.SMTPException as e:
                Attempt.objects.create(
                    mailing=mailing,
                    status='failure',
                    server_response=str(e)
                )
                logger.error(f'Failed to send mailing to {client.contact_email}: {str(e)}')
            except Exception as e:
                Attempt.objects.create(
                    mailing=mailing,
                    status='failure',
                    server_response=str(e)
                )
                logger.error(f'Unexpected error while sending mailing to {client.contact_email}: {str(e)}')
