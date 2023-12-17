from django.test import TestCase
from mailings.models import Client, Mailing, Message
from notifications.models import Notification

class ProjectIntegrationTest(TestCase):
    def test_project_interaction(self):
        # Тестирование взаимодействия между приложениями
        # Пример: создание объектов и проверка взаимодействия между моделями разных приложений

        # Создание клиента в приложении mailings
        client = Client.objects.create(phone_number='1234567890', mobile_operator_code='123', tag='Test', timezone='UTC')

        # Создание рассылки в приложении mailings
        mailing = Mailing.objects.create(start_time='2023-12-31T12:00:00Z', end_time='2023-12-31T13:00:00Z', message_text='Test message')

        # Создание уведомления в приложении notifications
        notification = Notification.objects.create(text='Test notification', status='Sent')

        # Создание сообщения в приложении mailings
        message = Message.objects.create(mailing=mailing, client=client, status='Sent')

        # Проверка взаимодействия между моделями
        self.assertEqual(client.tag, 'Test')
        self.assertEqual(mailing.message_text, 'Test message')
        self.assertEqual(notification.text, 'Test notification')
        self.assertEqual(message.status, 'Sent')

