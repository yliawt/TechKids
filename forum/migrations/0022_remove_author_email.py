# Generated by Django 2.2 on 2020-06-08 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_auto_20200607_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
    ]
