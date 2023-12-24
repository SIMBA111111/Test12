from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('config')

# Использование настроек Django из файла settings.py
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из приложений Django
celery_app.autodiscover_tasks()


@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')