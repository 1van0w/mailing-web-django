from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from .models import Mailing, MessageStatistics


def send_daily_statistics():
    # Логика для получения статистики за последние 24 часа
    start_time = datetime.now() - timedelta(days=1)
    end_time = datetime.now()

    processed_mailings = Mailing.objects.filter(start_time__range=(start_time, end_time))

    statistics_data = []
    for mailing in processed_mailings:
        statistics = MessageStatistics.objects.filter(mailing=mailing)
        statistics_data.append({
            'mailing': mailing,
            'statistics': statistics
        })

    # Формирование email с HTML-шаблоном
    html_message = render_to_string('email/statistics_email.html', {'statistics_data': statistics_data})
    plain_message = strip_tags(html_message)

    # Отправка email
    send_mail(
        'Daily Statistics',
        plain_message,
        'your_email@example.com',
        ['recipient@example.com'],
        html_message=html_message,
    )