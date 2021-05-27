from django.contrib import admin
from .models import SiteUser, Profile, Profession, ProfessionInstance


@admin.register(SiteUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'location', 'email', 'phone_number', 'email_verified', 'phone_verified', 'last_login',)
    list_filter = ('phone_verified', 'email_verified', 'location', 'last_login',)
    ordering = ('username',)

    fieldsets = (
        (None, {
            'fields': (
                'username',
                ('first_name', 'last_name',),
                'birth_date',
                ('email', 'phone_number'),
                ('email_verified', 'phone_verified'),
                'location',
                'description',
            )
        }),
        ('Служебные', {
            'fields': (
                'password',
                'is_staff',
                'is_active',
                'date_joined',
                'last_login',
                'groups',
                'user_permissions',
            )
        })
    )


class ProfessionInstanceInline(admin.TabularInline):
    model = ProfessionInstance
    extra = 0


@admin.register(ProfessionInstance)
class ProfessionInstanceAdmin(admin.ModelAdmin):
    list_display = ('userprofile', 'profession', 'rating')
    list_filter = ('profession', 'userprofile')
    ordering = ('userprofile', 'profession',)


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'id')
    inlines = [ProfessionInstanceInline]
    ordering = ('user',)


@admin.register(Profession)
class Profession(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
