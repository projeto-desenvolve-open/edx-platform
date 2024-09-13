from django.urls import path
from openedx.core.djangoapps.celery_repro.views import run_celery_task

urlpatterns = [
    path('', run_celery_task, name='celery_repro'),
]
