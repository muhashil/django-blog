from django.db import models
from accounts.models import Author

class ArticleManager(models.Manager):
    def featured(self):
        return super().filter(featured=True)

    def with_category(self, category):
        return super().filter(kategori=category)

class Category(models.Model):
    judul = models.CharField(max_length=250, unique=True,
                             verbose_name='Judul Kategori')
    slug = models.SlugField(max_length=250, unique=True)
    deskripsi = models.TextField(blank=True, verbose_name='Deskripsi Kategori')

    class Meta:
        ordering = ['judul']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.judul


class Article(models.Model):
    judul = models.CharField(max_length=250, unique=True,
                             verbose_name='Judul')
    slug = models.SlugField(max_length=250, unique=True)
    isi = models.TextField(blank=True, verbose_name='Isi')
    gambar = models.ImageField(upload_to='artikel/', blank=True)
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)
    penulis = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ArticleManager()

    class Meta:
        ordering = ['modified_date']
        get_latest_by = 'pub_date'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        indexes = [
            models.Index(fields=['judul'], name='judul_index'),
            models.Index(fields=['penulis'], name='penulis_index')
        ]

    def __str__(self):
        return self.judul

