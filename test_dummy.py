from mock import MagicMock
import smtplib
import unittest

from alert import EmailSending


class TestDummySendEmail(unittest.TestCase):
    def test_connection_refused(self):
        email_sender = EmailSending()
        success = email_sender.send_message(MagicMock(), MagicMock())
        self.assertFalse(success)
