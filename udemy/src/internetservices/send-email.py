""" smtp: Simple Mail Transfer Protocol library
    like HTTP but for email"""
import smtplib

sender = 'rzuniga64@gmail.com'
receivers = 'raul.zuniga@g.austincc.edu'
message = 'test message sent from Python'
username = 'rzuniga64'
password = 'cinnamon92'
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(sender, receivers, message)
    server.quit()
except SMTPException:
    print ("Error: unable to send email")
