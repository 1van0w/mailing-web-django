from django.shortcuts import render
from .models import MailingStatistics

def mailing_statistics_view(request):
    # Получение статистики по выполненным рассылкам
    mailing_stats = MailingStatistics.objects.all()
    return render(request, 'mailing_statistics.html', {'mailing_stats': mailing_stats})
