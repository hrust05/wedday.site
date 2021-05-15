from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(
        'Идентификатор',
        primary_key=True,
        default=uuid.uuid4,
        help_text='Уникальный идентификатор данного профиля')
    location = models.fields.CharField(
        'Расположение',
        max_length=500,
        blank=True,
        help_text='Укажите наименование ближайшего к Вам населённого пункта (необязательный параметр)')
    birth_date = models.DateField(
        'Дата рождения',
        null=True,
        blank=True,
        help_text='Укажите Вашу дату рождения (неоябзательный параметр)')
    email_confirmed = models.BooleanField(
        'Верифицирован',
        default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?7?\d{9,9}$',
        message="Телефонный номер должен быть введён в формате: '+79999999999'")
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_regex],
        max_length=10,
        blank=True,
        help_text='Введите номер телефона в формате: +79999999999')

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.user.id)])

    def __str__(self):
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} ({1})'.format(self.user.email, self.uuid)


class Profession(models.Model):
    name = models.CharField(
        'Профессия',
        max_length=500,
        help_text='Введите название добавляемой на сайт профессии')

    def __str__(self):
        return self.name


class UserProfessionInstance(models.Model):
    userprofile = models.ForeignKey(
        'Profile',
        on_delete=models.SET_NULL,
        null=True,
        help_text='Уникальный идентификатор профиля специалиста',
    )
    profession = models.OneToOneField(
        Profession,
        help_text='Одна из профессий, которыми обладает данный пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.profession, self.userprofile)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



