from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'tags', 'tags_list', 'created_at', 'author_name', 'image']
    
    def get_tags_list(self, obj):
        return [tag.strip() for tag in obj.tags.split(',') if tag.strip()]

class ArticleViewSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
    
    def get_tags_list(self, obj):
        return [tag.strip() for tag in obj.tags.split(',') if tag.strip()]