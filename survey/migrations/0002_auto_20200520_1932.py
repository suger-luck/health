# Generated by Django 3.0.4 on 2020-05-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='submit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='提交时间'),
        ),
    ]
