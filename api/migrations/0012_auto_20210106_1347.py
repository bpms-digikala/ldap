# Generated by Django 3.1.4 on 2021-01-06 10:17

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201228_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='success',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='teamwork',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='success',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='teamwork',
        ),
        migrations.AddField(
            model_name='reference',
            name='n_name',
            field=models.CharField(default='name', max_length=200, validators=[api.validators.namfarsi]),
        ),
    ]
