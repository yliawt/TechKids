# Generated by Django 2.2 on 2020-06-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0032_auto_20200616_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
