from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informasi Penulis', {
            'fields': (('first_name', 'last_name'),
                       'username', 'email',  'foto', 'quote', 'last_login', 'date_joined')
        }),
        ('Informasi Lainnya', {
            'fields': ('groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')
        })
    )
    exclude = ('password',)


admin.site.register(Author, AuthorAdmin)
