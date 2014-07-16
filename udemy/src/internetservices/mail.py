import smtplib
import imaplib
import os

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


def read():
    mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = 'mcmillanadmin'
    password = 'meredith1'
    mailserver.login(username, password)
    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')
    print(data[0][1])
    mailserver.close()
    mailserver.logout()

    choice = input("Epress x to clear screen: ")
    if choice == "x'":
        os.system("cls")


def send():
    fromaddr = input("Enter your email address: ")
    toaddr = input("Enter the receiver's email address: ")
    subject = input("Enter the subject: ")
    text = input("Enter the subject: ")
    username = input("Enter your user name: ")
    password = input("Enter our password: ")
    msg = MIMIMultipart()
    msg('From') = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

while 1:
    os.system("cls")
    print("Email Program")
    print("")
    print("1. Read email")
    print("2. Send email")
    print("3. Exit")
    print("")
    choice = input("Enter a choice: ")
    if choice == "1":
        read()
    elif choice == "2":
        send()
    elif choice == "3":
        break
