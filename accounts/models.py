from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    email = models.EmailField(
        max_length=250, unique=True, verbose_name='Alamat Email')
    foto = models.ImageField(
        upload_to='penulis/', blank=True, verbose_name='Foto Profil')
    quote = models.TextField(blank=True, verbose_name='Favorit Quote')

    def __str__(self):
        return self.email
