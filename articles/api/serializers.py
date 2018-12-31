from rest_framework import serializers
from articles.models import Article, Category
from accounts.models import Author
from django.utils.text import slugify


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('slug', )
                
    def create(self, validated_data):
        article = Article(
            judul=validated_data['judul'],
            slug=slugify(validated_data['judul']),
            isi=validated_data['isi'],
            kategori=validated_data['kategori'],
            penulis=validated_data['penulis'],
        )
        article.save()
        return article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'username', 'email', 'foto', 'quote')
