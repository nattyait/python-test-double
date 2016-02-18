import smtplib

class EmailSending: 
	def send_message(self, users, message):
		smtpobj = smtplib.SMTP('localhost', 1025)
		status = smtpobj.sendmail('user', users, message)
		smtpobj.quit()


	def say_in_email(self, name, recipient):
		hellomessage = self.hello(name) + ". You are " + self.hello(name)
		message = 'Ah ' + hellomessage
		self.send_message(recipient, message)
		return message

	def hello(self, name):
		return "hello %s" % name

