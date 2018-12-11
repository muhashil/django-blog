from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    foto = models.ImageField(
        upload_to='penulis/', blank=True, verbose_name='Foto Profil')
    quote = models.TextField(blank=True, verbose_name='Favorit Quote')

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
