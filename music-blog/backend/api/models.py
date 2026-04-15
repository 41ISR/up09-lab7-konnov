from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    desc = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Содержание')
    tags = models.CharField(
        max_length=255, 
        verbose_name='Теги',
        help_text='Строка с тегами, разделенными запятыми (например: хип-хоп, рэп, музыка)'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='articles',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='articles/', 
        blank=True, 
        null=True,
        verbose_name='Изображение'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]