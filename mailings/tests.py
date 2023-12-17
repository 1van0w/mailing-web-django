from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from .models import Mailing
import uuid


class MailingModelTest(TestCase):
    def test_mailing_creation(self):
        unique_id = uuid.uuid4()
        start_time = timezone.now()
        message_text = "text"

        mailing = Mailing.objects.create(
            unique_id=unique_id,
            start_time=start_time,
            message_text=message_text
        )

        self.assertIsInstance(mailing, Mailing)
        self.assertEqual(mailing.start_time, start_time)
        self.assertEqual(mailing.message_text, message_text)
        self.assertIsNone(mailing.end_time)  # Проверка, что время окончания равно None при создании

    def test_end_time_auto_set(self):
        start_time_past = timezone.now() - timezone.timedelta(days=1)
        start_time_future = timezone.now() + timezone.timedelta(days=1)

        mailing_past = Mailing.objects.create(start_time=start_time_past)
        mailing_future = Mailing.objects.create(start_time=start_time_future)

        self.assertIsNotNone(
            mailing_past.end_time)  # Проверка, что время окончания установлено при времени начала в прошлом
        self.assertIsNone(mailing_future.end_time)  # Проверка, что время окончания None при времени начала в будущем