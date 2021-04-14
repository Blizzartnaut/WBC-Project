# Generated by Django 3.1.7 on 2021-04-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Time Created')),
                ('burnerzone', models.IntegerField(verbose_name='BunerZone')),
                ('burner_1', models.IntegerField(verbose_name='Temperature')),
                ('burner_2', models.IntegerField(verbose_name='Temperature')),
                ('burner_3', models.IntegerField(verbose_name='Temperature')),
                ('burner_4', models.IntegerField(verbose_name='Temperature')),
                ('burner_5', models.IntegerField(verbose_name='Temperature')),
                ('burner_6', models.IntegerField(verbose_name='Temperature')),
                ('burner_7', models.IntegerField(verbose_name='Temperature')),
                ('burner_8', models.IntegerField(verbose_name='Temperature')),
                ('burner_9', models.IntegerField(verbose_name='Temperature')),
                ('burner_10', models.IntegerField(verbose_name='Temperature')),
                ('burner_11', models.IntegerField(verbose_name='Temperature')),
                ('burner_12', models.IntegerField(verbose_name='Temperature')),
                ('user', models.CharField(max_length=30, verbose_name='User')),
            ],
        ),
    ]