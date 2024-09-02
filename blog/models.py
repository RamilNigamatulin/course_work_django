from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from users.models import User


class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название заголовка",
        help_text="Введите название заголовка",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="URL-адрес",
        null=True,
        blank=True,
    )
    content = models.TextField(
        max_length=10000,
        verbose_name="Содержимое",
        help_text="Описание блога",
    )
    preview = models.ImageField(
        upload_to='photo/blog',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото',
    )
    created_date = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now,
    )
    published = models.BooleanField(
        verbose_name='Признак публикации',
        default=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Количество просмотров',
        default=0,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

