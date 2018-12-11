from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['judul', 'slug']
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'pub_date'


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis',
                    'kategori', 'modified_date', 'pub_date']
    readonly_fields = ('pub_date', 'modified_date')
    search_fields = ['judul']


admin.site.register(Category, CategoryAdmin)
