from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
import uuid


class SiteUser(AbstractUser):
    id = models.UUIDField(
        'Идентификатор',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Уникальный идентификатор данного пользователя')
    phone_regex = RegexValidator(
        regex=r'^\+?7?\d{9,10}$',
        message="Телефонный номер должен быть введён в формате: '+79999999999'")
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_regex],
        max_length=12,
        blank=True,
        help_text='Введите номер телефона в формате: +79999999999')
    phone_verified = models.BooleanField(
        'Телефон верифицирован',
        default=False)
    email_verified = models.BooleanField(
        'Адрес электронной почты верифицирован',
        default=False)
    location = models.fields.CharField(
        'Расположение',
        max_length=500,
        blank=True,
        help_text='Укажите наименование ближайшего к Вам населённого пункта (необязательный параметр)')
    birth_date = models.DateField(
        'Дата рождения',
        null=True,
        blank=True,
        help_text='Укажите Вашу дату рождения (необязательный параметр)')
    description = models.fields.TextField(
        'Резюме',
        blank=True,
        max_length=1000,
        help_text='Введите краткую информацию о себе (необязательно)')
    image_url = models.CharField(
        'Фото профиля',
        max_length=1000,
        blank=True,
        null=True,
        help_text='Фото профиля (необязательно)')
    insta_profile = models.CharField(
        'Профиль в инстаграм',
        max_length=500,
        blank=True,
        null=True,
        help_text='Имя профиля в инстаграм')
    insta_verified = models.BooleanField(
        'Профиль инстаграм подтверждён',
        default=False)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])

    def __str__(self):
        return '{0} (id = {1})'.format(self.username, self.id)


class Profile(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)
    id = models.UUIDField(
        'Идентификатор',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Уникальный идентификатор данного профиля')

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])

    def __str__(self):
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} ({1})'.format(self.user.username, self.user.email)


class Profession(models.Model):
    name = models.CharField(
        'Профессия',
        max_length=500,
        help_text='Введите название добавляемой на сайт профессии',
    )

    description = models.TextField(
        'Описание профессии',
        max_length=1000,
        null=True,
        blank=True,
        help_text='Краткое описание профессии',
    )

    def __str__(self):
        return self.name


class ProfessionInstance(models.Model):
    userprofile = models.ForeignKey(
        'Profile',
        on_delete=models.SET_NULL,
        null=True,
        help_text='Уникальный идентификатор профиля специалиста',
    )
    rating = models.IntegerField(
        'Рейтинг',
        null=True,
        help_text='Рейтинг специалиста в данной профессии'
    )
    profession = models.ForeignKey(
        'Profession',
        on_delete=models.SET_NULL,
        null=True
    )

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.userprofile.id)])

    def __str__(self):
        return '{0} {1}'.format(self.userprofile.user.username, self.profession)
