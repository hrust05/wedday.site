# Generated by Django 3.2.3 on 2021-05-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210528_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='description',
            field=models.TextField(blank=True, help_text='Краткое описание профессии', max_length=1000, null=True, verbose_name='Описание профессии'),
        ),
    ]
