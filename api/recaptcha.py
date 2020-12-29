from django.conf import settings
import requests


def callRecaptcha(value):
    r = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': settings.SECRET_CAPTCHA,
            'response': value,
        }
    )
    return r
