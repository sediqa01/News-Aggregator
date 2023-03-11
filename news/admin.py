from django.contrib import admin
from .models import Article, Author, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('news_overview', 'news_content')
    prepopulated_fields = {'slug': ('news_title',)}
    list_filter = ('published_status', 'created_on')
    search_fields = ['news_title', 'news_content']
    list_display = ('news_title', 'published_status', 'created_on')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['user']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']

