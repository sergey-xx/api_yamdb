from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_username


class User(AbstractUser):
    """Модель данных для пользователей."""
    class Role(models.TextChoices):
        """Роли пользователей."""
        ADMIN = 'admin', 'Администратор'
        MODERATOR = 'moderator', 'Модератор'
        USER = 'user', 'Пользователь'

    username = models.CharField(
        'Никнейм',
        max_length=150,
        unique=True,
        validators=[validate_username, ])
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=5,
        blank=True)
    email = models.EmailField('Почта', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField('Биография', blank=True)
    role = models.CharField(
        'Роль',
        max_length=25,
        choices=Role.choices,
        default=Role.USER
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"
        unique_together = ('username', 'email')

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    @property
    def is_user(self):
        return self.role == self.Role.USER

    def __str__(self):
        return self.username
