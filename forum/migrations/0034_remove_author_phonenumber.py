# Generated by Django 2.2 on 2020-06-16 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0033_author_is_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='phonenumber',
        ),
    ]