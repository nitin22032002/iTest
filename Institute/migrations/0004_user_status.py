# Generated by Django 3.2.9 on 2021-11-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0003_auto_20211120_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
