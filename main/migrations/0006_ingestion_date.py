# Generated by Django 2.2 on 2021-09-25 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210925_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingestion',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 25, 20, 48, 15, 983070), verbose_name='Дата'),
        ),
    ]
