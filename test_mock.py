import smtplib
import unittest
from alert import EmailSending
from mock import Mock, patch, call


class TestMockSendEmail(unittest.TestCase):
    def test_mock(self):
        real = EmailSending()
        real.send_message = Mock()
        real.say_in_email('natty', 'yoyo')
        real.send_message.assert_called_once_with('yoyo','Ah hello natty. You are hello natty')

    #spy record something
    def test_spy(self):
        real = EmailSending()
        real.send_message = Mock()
        real.hello = Mock()
        real.hello.return_value = 'hello mock'
        message = real.say_in_email('Natty', 'natty@natty.com')
        self.assertEqual(real.send_message.called, True)
        self.assertEqual(real.send_message.call_count, 1)
        self.assertEqual(message, 'Ah hello mock. You are hello mock')
        self.assertEqual(real.hello.call_count, 2)

    #stub
    def test_stub(self):
        with patch("smtplib.SMTP") as mock_smtp:
            real = EmailSending()
            real.send_message('natty', 'hello')
