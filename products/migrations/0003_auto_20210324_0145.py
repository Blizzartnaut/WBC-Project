# Generated by Django 2.1.5 on 2021-03-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
