import smtplib
import unittest
from alert import EmailSending
from mock import Mock


class fake_SMTP:
	calls = []
	
	def __init__(self, _server, _port):
		self.calls.append("__init__('%s', %d)" % (_server, _port) )

	def sendmail(self, _from, _to, _msg):
		self.calls.append("sendmail('%s', %s, <msg>)" % (_from, _to))

	def quit(self):
		self.calls.append("quit()")

setattr(smtplib, 'SMTP', fake_SMTP)

class TestFakeSendEmail(unittest.TestCase):
	
	def test_fake_smtp(self):
	    name = "Yoyo"
	    email = EmailSending()
	    email.send_message(['eradman@eradman.com'], name)
	    self.assertEqual(fake_SMTP.calls,
	        ["__init__('localhost', 1025)",
	        "sendmail('user', ['eradman@eradman.com'], <msg>)",
	        "quit()"])