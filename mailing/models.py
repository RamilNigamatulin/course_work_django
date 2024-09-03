from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """данные клиента"""

    contact_email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите электронную почту',
        unique=True,
    )
    surname = models.CharField(
        max_length=70,
        verbose_name='Фамилия',
        help_text='Введите Фамилию',
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        help_text='Введите Имя',
    )
    patronimic = models.CharField(
        **NULLABLE,
        max_length=70,
        verbose_name='Отчество',
        help_text='Ввeдите отчество',
    )
    comment = models.CharField(
        **NULLABLE,
        max_length=200,
        verbose_name='Комментарий',
        help_text='Введите комментарий',
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self ):
        return f'{self.contact_email}, {self.surname}, {self.name}'


class Mailing(models.Model):
    """настройка рассылки сообщений"""

    mailing_name = models.CharField(
        **NULLABLE,
        max_length=100,
        verbose_name='Название рассылки',
        help_text='Введите название рассылки',
    )
    periodicity = models.CharField(
        verbose_name='Периодичность рассылки',
        help_text='Выберите периодичность рассылки',
        choices=[
            ('60', 'Ежеминутно'),
            ('300', 'Каждые пять минут'),
            ('600', 'Каждые 10 минут'),
        ],
        max_length=50,
    )
    status = models.CharField(
        verbose_name='Статус рассылки',
        help_text='Выберите статус рассылки',
        choices=[
            ('completed', 'Завершена'),
            ('created', 'Создана'),
            ('launched', 'Запущена'),
        ],
        max_length=50,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('can_view_mailing', 'Могу просматривать любые рассылки'),
            ('can_view_users', 'Могу просматривать список пользователей'),
            ('can_block_users', 'Могу блокировать пользователей'),
            ('can_disable_mailings', 'Могу отключать рассылки'),
        ]

    def __str__(self):
        return f'{self.mailing_name}, {self.periodicity}, {self.status}'


class Message(models.Model):
    """сообщение для рассылки"""

    letter_subject = models.CharField(
        max_length=100,
        verbose_name='Тема письма',
        help_text='Введите тему письма',
    )
    text_letter = models.TextField(
       verbose_name='Текст письма',
       help_text='Введите текст письма',
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='Рассылка',
        **NULLABLE,
    )
    clients = models.ManyToManyField(
        Client,
        verbose_name='Клиенты',
        help_text='Выберите клиентов для рассылки',
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.letter_subject}, {self.text_letter}, {self.clients}'


class Attempt(models.Model):
    """попытка рассылки"""

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='Рассылка',
        help_text='Выберите рассылку',
    )
    attempt_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время последней попытки',
        help_text='Дата и время последней попытки',
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('success', 'Успешно'),
            ('failure', 'Неуспешно')
        ],
        verbose_name='Статус попытки',
    )
    server_response = models.TextField(
        **NULLABLE,
        verbose_name='Ответ почтового сервера',
        help_text='Ответ почтового сервера, если он был',
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        **NULLABLE,
    )

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'

    def __str__(self):
        return f'Попытка {self.attempt_time} - {self.status}'



@receiver(post_save, sender=Mailing)
def send_mailing_emails(sender, instance, **kwargs):
    if instance.status == 'created' or instance.status == 'updated':
        messages = Message.objects.filter(mailing=instance)
        for message in messages:
            for client in message.clients.all():
                try:
                    send_mail(
                        subject=message.letter_subject,
                        message=message.text_letter,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[client.contact_email],
                        fail_silently=False,
                    )
                    Attempt.objects.create(
                        mailing=instance,
                        status='success',
                        server_response='200 OK'
                    )
                except Exception as e:
                    Attempt.objects.create(
                        mailing=instance,
                        status='failure',
                        server_response=str(e)
                    )