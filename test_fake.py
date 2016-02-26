import smtplib
import unittest

from alert import EmailSender


class fake_SMTP:
    calls = []

    def __init__(self, _server, _port):
        self.calls.append("__init__('%s', %d)" % (_server, _port) )

    def sendmail(self, _from, _to, _msg):
        self.calls.append("sendmail('%s', %s, <msg>)" % (_from, _to))

    def quit(self):
        self.calls.append("quit()")


class TestFakeSendEmail(unittest.TestCase):
    def setUp(self):
        self.real_SMTP = getattr(smtplib, 'SMTP')
        setattr(smtplib, 'SMTP', fake_SMTP)

    def tearDown(self):
        setattr(smtplib, 'SMTP', self.real_SMTP)

    def test_fake(self):
        name = 'Yoyo'
        email = EmailSender()
        email.send_message(['eradman@eradman.com'], name)
        self.assertEqual(fake_SMTP.calls,
            ["__init__('localhost', 1025)",
            "sendmail('user', ['eradman@eradman.com'], <msg>)",
            "quit()"]
        )
