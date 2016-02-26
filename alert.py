import socket
import smtplib


class EmailSending:
    def send_message(self, users, message):
        try:
            smtpobj = smtplib.SMTP('localhost', 1025)
            smtpobj.sendmail('user', users, message)
            smtpobj.quit()
            return True
        except socket.error:
            return False

    def say_in_email(self, name, recipient):
        hellomessage = self.hello(name) + '. You are ' + self.hello(name)
        message = 'Ah ' + hellomessage
        self.send_message(recipient, message)
        return message

    def hello(self, name):
        return "hello %s" % name
