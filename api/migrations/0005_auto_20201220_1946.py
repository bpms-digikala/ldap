# Generated by Django 3.1.4 on 2020-12-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201220_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='improve',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='point',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
