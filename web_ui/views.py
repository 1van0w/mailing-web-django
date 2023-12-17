from django.shortcuts import render
from .models import Mailing, MessageStatistics

def mailing_management(request):
    mailings = Mailing.objects.all()
    # Другие операции, такие как создание, обновление и удаление рассылок
    return render(request, 'mailing_management.html', {'mailings': mailings})

def message_statistics(request, mailing_id):
    mailing = Mailing.objects.get(pk=mailing_id)
    statistics = MessageStatistics.objects.filter(mailing=mailing)
    # Логика для получения статистики по сообщениям для данной рассылки
    return render(request, 'message_statistics.html', {'mailing': mailing, 'statistics': statistics})
