from mock import MagicMock, patch
import smtplib
import unittest

from alert import EmailSender


class TestMockSendEmail(unittest.TestCase):
    def setUp(self):
        self.email_sender = EmailSender()
        self.actual_send_message = self.email_sender.send_message
        self.actual_say_in_email = self.email_sender.say_in_email
        self.actual_hello = self.email_sender.hello

    def tearDown(self):
        self.email_sender.send_message = self.actual_send_message
        self.email_sender.say_in_email = self.actual_say_in_email
        self.email_sender.hello = self.actual_hello

    def test_mock(self):
        self.email_sender.send_message = MagicMock()
        self.email_sender.say_in_email('natty', 'yoyo')
        self.email_sender.send_message.assert_called_once_with(
            'yoyo',
            'Ah hello natty. You are hello natty'
        )

    def test_spy(self):
        self.email_sender.send_message = MagicMock()
        self.email_sender.hello = MagicMock()
        self.email_sender.hello.return_value = 'hello mock'

        message = self.email_sender.say_in_email('Natty', 'natty@natty.com')

        self.assertEqual(message, 'Ah hello mock. You are hello mock')
        self.assertTrue(self.email_sender.send_message.called)
        self.assertEqual(self.email_sender.send_message.call_count, 1)
        self.assertEqual(self.email_sender.hello.call_count, 2)

    def test_stub(self):
        with patch("smtplib.SMTP") as mock_smtp:
            self.email_sender.send_message('natty', 'hello')

    def test_dummy(self):
        success = self.email_sender.send_message(MagicMock(), MagicMock())
        self.assertFalse(success)
