from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

# بررسی فرمت صحیح کد ملی


def codemeli(value):
    if not(re.match("^\\d{10}$", value)) or value == '0000000000' or value == '1111111111' or value == '2222222222' or value == '3333333333' or value == '4444444444' or value == '5555555555' or value == '6666666666' or value == '7777777777' or value == '8888888888' or value == '9999999999':
        raise ValidationError(
            _('%(value)s کد ملی معتبری نمی‌باشد'),
            params={'value': value},
        )
    checking = int(value[9:10])
    sum = 0
    x = range(9)
    for i in x:
        sum += int(value[i:i+1])*(10 - i)
    sum %= 11
    if (sum < 2 and checking == sum) or (sum >= 2 and checking + sum == 11):
        return value
    else:
        raise ValidationError(
            _('%(value)s کد ملی معتبری نمی‌باشد.'),
            params={'value': value},
        )

# فقط از نام های فارسی در فیلد نام استفاده شود


def namfarsi(value):
    if not(re.match("^[\u0600-\u06FF\\s]+$", value)):
        raise ValidationError(
            _('%(value)s حروف فارسی نمی‌باشد.'),
            params={'value': value},
        )
    else:
        return value


def namOrnull(value):
    if not(re.match("^[\u0600-\u06FF\\s]+$", value)) and not(re.match("^$|\\s+", value)):
        raise ValidationError(
            _('%(value)s حروف فارسی نمی‌باشد.'),
            params={'value': value},
        )
    else:
        return value


def mobile(value):
    if not(re.match("^(?:\\+?98)?09[0-9]\\d{8}$", value)):
        raise ValidationError(
            _('%(value)s شماره موبایل معتبر نمی‌باشد.'),
            params={'value': value},
        )
    else:
        return value


def emailcheck(value):
    if not(re.match("[^@]+@[^@]+\\.[^@]+", value)):
        raise ValidationError(
            _('%(value)s ایمیل معتبر نمی‌باشد.'),
            params={'value': value},
        )
    else:
        return value


def likert(value):
    if not(re.match("^[1-5]$", str(value))):
        raise ValidationError(
            _('%(value)s گزینه انتخابی معتبر نیست.'),
            params={'value': value},
        )
    else:
        return value
