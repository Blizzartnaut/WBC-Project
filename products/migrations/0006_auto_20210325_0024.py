# Generated by Django 2.1.5 on 2021-03-25 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210325_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 3, 25, 0, 24, 6, 223363)),
        ),
    ]
