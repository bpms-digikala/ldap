from django.db import models
from .validators import codemeli, namfarsi, mobile, emailcheck, likert, namOrnull


class Reference(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    email = models.CharField(max_length=50, validators=[emailcheck])
    codemelli = models.CharField(max_length=10, validators=[
                                 codemeli], unique=True)
    m_name = models.CharField(max_length=200, validators=[namfarsi])
    m_email = models.CharField(max_length=50, validators=[emailcheck])
    m_mobile = models.CharField(max_length=20, validators=[mobile])
    m_uuid = models.CharField(max_length=8)
    p_name = models.CharField(max_length=200, validators=[namfarsi])
    p_email = models.CharField(max_length=50, validators=[emailcheck])
    p_mobile = models.CharField(max_length=20, validators=[mobile])
    p_uuid = models.CharField(max_length=8)


class Manager(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    reference = models.OneToOneField(Reference, on_delete=models.CASCADE)
    job = models.CharField(max_length=200, validators=[namfarsi])
    detail = models.CharField(max_length=255, validators=[namfarsi])
    success = models.CharField(max_length=255, validators=[namfarsi])
    creativity = models.CharField(max_length=255, validators=[namfarsi])
    teamwork = models.CharField(max_length=255, validators=[namfarsi])
    strong = models.CharField(max_length=255, validators=[namfarsi])
    improve = models.CharField(max_length=255, validators=[
                               namOrnull], blank=True)
    separation = models.CharField(
        max_length=255, validators=[namfarsi])
    suggest = models.IntegerField(validators=[likert])
    point = models.CharField(max_length=255, validators=[
                             namOrnull], blank=True)


class Partner(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    reference = models.OneToOneField(Reference, on_delete=models.CASCADE)
    job = models.CharField(max_length=200, validators=[namfarsi])
    detail = models.CharField(max_length=255, validators=[namfarsi])
    success = models.CharField(max_length=255, validators=[namfarsi])
    creativity = models.CharField(max_length=255, validators=[namfarsi])
    teamwork = models.CharField(max_length=255, validators=[namfarsi])
    strong = models.CharField(max_length=255, validators=[namfarsi])
    improve = models.CharField(max_length=255, validators=[
                               namOrnull], blank=True)
    separation = models.CharField(max_length=255, validators=[namfarsi])
    suggest = models.IntegerField(validators=[likert])
    point = models.CharField(max_length=255, validators=[
                             namOrnull], blank=True)
