from django.test import TestCase
from .models import MailingStatistics
from mailings.models import Mailing

class MailingStatisticsModelTest(TestCase):
    def setUp(self):
        self.mailing = Mailing.objects.create(
            start_time='2023-12-31T12:00:00Z',
            message_text='Test message'

        )

    def test_mailing_statistics_creation(self):
        mailing_statistics = MailingStatistics.objects.create(
            mailing=self.mailing,
            sent_messages=10,
            successful_deliveries=8

        )
        self.assertTrue(isinstance(mailing_statistics, MailingStatistics))
        self.assertEqual(mailing_statistics.mailing, self.mailing)
        self.assertEqual(mailing_statistics.sent_messages, 10)
        self.assertEqual(mailing_statistics.successful_deliveries, 8)

