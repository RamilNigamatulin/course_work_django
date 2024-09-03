
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views.generic import UpdateView, ListView
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse_lazy



class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='photo/avatars/',
        verbose_name='Аватар',
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Введите номер телефона',
    )
    country = models.CharField(
        max_length=150,
        verbose_name='Страна',
        help_text='Введите название страны',
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        blank=True,
        null=True,
        help_text='Токен для авторизации',
    )
    is_blocked = models.BooleanField(
        default=False,
        verbose_name='Блокировка',
        help_text='Отключает доступ к аккаунту',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
