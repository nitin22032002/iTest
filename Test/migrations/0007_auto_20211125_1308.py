# Generated by Django 3.2.9 on 2021-11-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0006_alter_paper_test_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='test_end',
            field=models.CharField(default='2021-11-25 13:08:21.593980', max_length=100),
        ),
        migrations.AlterField(
            model_name='paper',
            name='test_start',
            field=models.CharField(default='2021-11-25 13:08:21.593980', max_length=100),
        ),
    ]