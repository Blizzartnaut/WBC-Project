# Generated by Django 2.1.5 on 2021-03-25 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210324_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.DateField(default=datetime.date(2021, 3, 25)),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 3, 25, 0, 17, 36, 530709)),
        ),
    ]
