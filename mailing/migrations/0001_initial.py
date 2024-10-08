# Generated by Django 4.2 on 2024-08-28 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(help_text='Введите электронную почту', max_length=254, unique=True, verbose_name='Электронная почта')),
                ('surname', models.CharField(help_text='Введите Фамилию', max_length=70, verbose_name='Фамилия')),
                ('name', models.CharField(help_text='Введите Имя', max_length=50, verbose_name='Имя')),
                ('patronimic', models.CharField(blank=True, help_text='Ввeдите отчество', max_length=70, null=True, verbose_name='Отчество')),
                ('comment', models.CharField(blank=True, help_text='Введите комментарий', max_length=200, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(help_text='Введите дату и время первой отправки рассылки', verbose_name='Дата и время первой отправки рассылки')),
                ('periodicity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], help_text='Выберите периодичность рассылки', max_length=50, verbose_name='Периодичность рассылки(раз в день, раз в неделю, раз в месяц)')),
                ('status', models.CharField(choices=[('completed', 'Завершена'), ('created', 'Создана'), ('launched', 'Запущена')], help_text='Выберите статус рассылки', max_length=50, verbose_name='Статус рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_subject', models.CharField(help_text='Введите тему письма', max_length=100, verbose_name='Тема письма')),
                ('text_letter', models.TextField(help_text='Введите текст письма', verbose_name='Текст письма')),
                ('clients', models.ManyToManyField(help_text='Выберите клиентов для рассылки', to='mailing.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(help_text='Выберите статус рассылки', on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_time', models.DateTimeField(auto_now_add=True, help_text='Дата и время последней попытки', verbose_name='Дата и время последней попытки')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failure', 'Неуспешно')], help_text='Выберите статус попытки', max_length=20, verbose_name='Статус попытки')),
                ('server_response', models.TextField(blank=True, help_text='Ответ почтового сервера, если он был', null=True, verbose_name='Ответ почтового сервера')),
                ('mailing', models.ForeignKey(help_text='Выберите рассылку', on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
