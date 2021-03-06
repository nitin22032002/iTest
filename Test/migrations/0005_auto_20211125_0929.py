# Generated by Django 3.2.9 on 2021-11-25 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0004_auto_20211125_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='question_attempt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='question_left',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='question_wrong',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='paper',
            name='test_start',
            field=models.DateField(default=datetime.datetime(2021, 11, 25, 9, 29, 5, 395248)),
        ),
    ]
