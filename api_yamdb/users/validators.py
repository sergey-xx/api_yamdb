import re

from django.core.exceptions import ValidationError


def validate_username(username):

    pattern = r'^[\w.@+-]+$'
    if username == 'me' or not re.search(pattern, username):
        raise ValidationError(
            'Имя не может содержать специальные символы и не равно "me"')
