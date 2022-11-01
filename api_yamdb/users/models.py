from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import UserameValidation


USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'

ROLE_CHOICES = [
    (USER, USER),
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR)
]


class User(AbstractUser):
    """Кастомная модель пользователя."""
    username = models.CharField(
        'Имя пользователя',
        validators = UserameValidation,
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        'Email пользователя',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        null=True,
        blank=False
    )



# Create your models here.
