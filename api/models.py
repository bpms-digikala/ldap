from django.db import models
from datetime import datetime
from .validators import codemeli, namfarsi, mobile, emailcheck


class Reference(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=50, validators=[emailcheck])
    codemelli = models.CharField(max_length=10, validators=[
                                 codemeli], unique=True)
    m_name = models.CharField(max_length=200, validators=[namfarsi])
    m_email = models.CharField(max_length=50, validators=[emailcheck])
    m_mobile = models.CharField(max_length=20, validators=[mobile])
    p_name = models.CharField(max_length=200, validators=[namfarsi])
    p_email = models.CharField(max_length=50, validators=[emailcheck])
    p_mobile = models.CharField(max_length=20, validators=[mobile])
