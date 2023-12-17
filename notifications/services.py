from .models import Notification
from mailings.models import Client, Mailing, Message
from datetime import datetime

# Логика для работы с клиентами
def add_client(phone_number, mobile_operator_code, tag, timezone):
    return Client.objects.create(phone_number=phone_number, mobile_operator_code=mobile_operator_code, tag=tag, timezone=timezone)

def update_client(client_id, **kwargs):
    Client.objects.filter(id=client_id).update(**kwargs)

def delete_client(client_id):
    Client.objects.filter(id=client_id).delete()

# Логика для работы с рассылками
def create_mailing(start_time, end_time, message_text, client_properties):
    return Mailing.objects.create(start_time=start_time, end_time=end_time, message_text=message_text, client_properties=client_properties)

def get_general_mailing_statistics():
    # Получение общей статистики по рассылкам
    return Mailing.objects.values('status').annotate(total_count=models.Count('id'))

def get_detailed_mailing_statistics(mailing_id):
    # Получение детальной статистики отправленных сообщений по конкретной рассылке
    return Message.objects.filter(mailing_id=mailing_id).values('status').annotate(total_count=models.Count('id'))

def update_mailing(mailing_id, **kwargs):
    Mailing.objects.filter(id=mailing_id).update(**kwargs)

def delete_mailing(mailing_id):
    Mailing.objects.filter(id=mailing_id).delete()

# Логика для отправки уведомлений через внешнее API
def send_notification(text):
    notification = Notification.objects.create(text=text, status='Sent', sent_at=datetime.now())
    return notification
