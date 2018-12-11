from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['judul', 'slug']
    prepopulated_fields = {'slug': ('judul',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis',
                    'kategori', 'featured', 'modified_date', 'pub_date']
    list_editable = ['featured']
    prepopulated_fields = {'slug': ('judul',)}
    readonly_fields = ('likes', 'pub_date', 'modified_date')
    search_fields = ['judul']
    date_hierarchy = 'pub_date'


admin.site.register(Article, ArticleAdmin)
