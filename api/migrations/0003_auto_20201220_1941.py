# Generated by Django 3.1.4 on 2020-12-20 16:11

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201220_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='improve',
            field=models.CharField(max_length=255, null=True, validators=[
                                   api.validators.namfarsi]),
        ),
        migrations.AlterField(
            model_name='partner',
            name='point',
            field=models.CharField(max_length=255, null=True, validators=[
                                   api.validators.namfarsi]),
        ),
    ]
