# Generated by Django 3.2.3 on 2021-05-15 23:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='Верифицирован'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Введите номер телефона в формате: +79999999999', max_length=10, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть введён в формате: '+79999999999'", regex='^\\+?7?\\d{9,9}$')], verbose_name='Номер телефона'),
        ),
    ]