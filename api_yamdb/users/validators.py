import re
from django.core.exceptions import ValidationError


class UserameValidation:
    """Валидация username."""
    def validate_username(self, username):
        pattern = re.compile(r'^[\w.@+-]+\z')
        if pattern.fullmatch(username) is None:
            match = re.split(pattern, username)
            symbol = ''.join(match)
            raise ValidationError(
                f'Нелья использовать символы {symbol}'
            )
        elif username == 'me':
            raise ValidationError(
            'Нельзя использовать имя пользователя "me"'
            )
        return username
