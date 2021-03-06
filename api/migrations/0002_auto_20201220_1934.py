# Generated by Django 3.1.4 on 2020-12-20 16:04

import api.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='email',
            field=models.CharField(max_length=50, validators=[
                                   api.validators.emailcheck]),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(
                    blank=True, default=datetime.datetime.now)),
                ('job', models.CharField(max_length=200,
                                         validators=[api.validators.namfarsi])),
                ('detail', models.CharField(max_length=255,
                                            validators=[api.validators.namfarsi])),
                ('success', models.CharField(max_length=255,
                                             validators=[api.validators.namfarsi])),
                ('creativity', models.CharField(
                    max_length=255, validators=[api.validators.namfarsi])),
                ('teamwork', models.CharField(max_length=255,
                                              validators=[api.validators.namfarsi])),
                ('strong', models.CharField(max_length=255,
                                            validators=[api.validators.namfarsi])),
                ('improve', models.CharField(max_length=255,
                                             validators=[api.validators.namfarsi])),
                ('separation', models.CharField(
                    max_length=255, validators=[api.validators.namfarsi])),
                ('suggest', models.IntegerField(
                    validators=[api.validators.likert])),
                ('point', models.CharField(max_length=255,
                                           validators=[api.validators.namfarsi])),
                ('reference', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='api.reference')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(
                    blank=True, default=datetime.datetime.now)),
                ('job', models.CharField(max_length=200,
                                         validators=[api.validators.namfarsi])),
                ('detail', models.CharField(max_length=255,
                                            validators=[api.validators.namfarsi])),
                ('success', models.CharField(max_length=255,
                                             validators=[api.validators.namfarsi])),
                ('creativity', models.CharField(
                    max_length=255, validators=[api.validators.namfarsi])),
                ('teamwork', models.CharField(max_length=255,
                                              validators=[api.validators.namfarsi])),
                ('strong', models.CharField(max_length=255,
                                            validators=[api.validators.namfarsi])),
                ('improve', models.CharField(max_length=255,
                                             validators=[api.validators.namfarsi])),
                ('separation', models.CharField(
                    max_length=255, validators=[api.validators.namfarsi])),
                ('suggest', models.IntegerField(
                    validators=[api.validators.likert])),
                ('point', models.CharField(max_length=255,
                                           validators=[api.validators.namfarsi])),
                ('reference', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='api.reference')),
            ],
        ),
    ]
