from django.db import models

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

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self ):
        return f'{self.contact_email}, {self.surname}, {self.name}'


class Mailing(models.Model):
    """настройка расслыки сообщений"""

    start_date = models.DateTimeField(
        verbose_name='Дата и время первой отправки рассылки',
        help_text='Введите дату и время первой отправки рассылки',
    )
    periodicity = models.CharField(
        verbose_name='Периодичность рассылки(раз в день, раз в неделю, раз в месяц)',
        help_text='Выберите периодичность рассылки',
        choices=[
            ('daily', 'Ежедневно'),
            ('weekly', 'Еженедельно'),
            ('monthly', 'Ежемесячно'),
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

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.start_date}, {self.periodicity}, {self.status}'


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
    message = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='Рассылка',
        help_text='Выберите статус рассылки',
    )
    clients = models.ManyToManyField(
        Client,
        verbose_name='Клиенты',
        help_text='Выберите клиентов для рассылки',
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.letter_subject}, {self.text_letter}, {self.message}, {self.clients}'


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
        help_text='Выберите статус попытки',
    )
    server_response = models.TextField(
        blank=True,
        null=True,
        verbose_name='Ответ почтового сервера',
        help_text='Ответ почтового сервера, если он был',
    )

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'

    def __str__(self):
        return f'Попытка {self.attempt_time} - {self.status}'