# Generated by Django 3.1 on 2020-10-11 21:24

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201011_2123'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]