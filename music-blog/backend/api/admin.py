from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'get_tags_display']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    
    def get_tags_display(self, obj):
        return obj.tags
    get_tags_display.short_description = 'Теги'