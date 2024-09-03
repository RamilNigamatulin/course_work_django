from django.apps import AppConfig
import threading
import logging


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        if not threading.current_thread() == threading.main_thread():
            return

        from django.apps import apps
        if not apps.ready:
            return

        from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
        from mailing.services import send_mailing

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        @register_job(scheduler, "interval", seconds=10)
        def test_job():
            try:
                send_mailing()
            except Exception as e:
                logging.error(f"Error in job: {e}")
                raise e

        register_events(scheduler)
        scheduler.start()
        logging.info("Scheduler started!")