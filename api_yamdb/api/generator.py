from random import randint

from django.conf import settings
from django.core.mail import send_mail


def get_confirmation_code():
    """Генерирация кода подтверждения."""

    return randint(
        settings.CONF_MIN,
        settings.CONF_MAX
    )


def send_confirmation_code(user):
    """
    Функция отпарвки кода подтверждения.
    """
    send_mail(
        subject='Код подтверждения.',
        message=(
            f'Добро пожаловать, {user.username}! '
            f'Ваш код подтверждения {user.confirmation_code}'
        ),
        from_email=settings.FROM_EMAIL,
        recipient_list=[user.email]
    )
