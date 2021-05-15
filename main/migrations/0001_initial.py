# Generated by Django 3.2.3 on 2021-05-15 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название добавляемой на сайт профессии', max_length=500, verbose_name='Профессия')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Уникальный идентификатор данного профиля', primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('location', models.CharField(blank=True, help_text='Укажите наименование ближайшего к Вам населённого пункта (необязательный параметр)', max_length=500, verbose_name='Расположение')),
                ('birth_date', models.DateField(blank=True, help_text='Укажите Вашу дату рождения (неоябзательный параметр)', null=True, verbose_name='Дата рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfessionInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.OneToOneField(help_text='Одна из профессий, которыми обладает данный пользователь', on_delete=django.db.models.deletion.CASCADE, to='main.profession')),
                ('userprofile', models.ForeignKey(help_text='Уникальный идентификатор профиля специалиста', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.profile')),
            ],
        ),
    ]