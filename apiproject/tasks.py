

from celery import shared_task
from .statistics_service import send_daily_statistics

@shared_task
def send_daily_statistics_task():
    send_daily_statistics()
