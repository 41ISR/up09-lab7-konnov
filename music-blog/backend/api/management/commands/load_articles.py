import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Article
from datetime import datetime

class Command(BaseCommand):
    help = 'Load articles from data.json'

    def handle(self, *args, **kwargs):
        # Создаем тестового пользователя если нет
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com'}
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write('Создан пользователь admin (пароль: admin123)')

        # Загружаем данные
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for article_data in data['articles']:
            article, created = Article.objects.get_or_create(
                title=article_data['title'],
                defaults={
                    'desc': article_data['desc'],
                    'content': article_data['content'],
                    'tags': ', '.join(article_data['tags']),
                    'created_at': datetime.strptime(article_data['date'], '%Y-%m-%d'),
                    'author': user,
                }
            )
            if created:
                count += 1

        self.stdout.write(f'Загружено {count} статей')