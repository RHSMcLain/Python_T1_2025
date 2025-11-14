import smtplib, ssl
from getpass import getpass
from email.message import EmailMessage

port = 465
server = "mclainonline.com"
usename = "student"
password = getpass("enter your password")

context = ssl._create_unverified_context()
with smtplib.SMTP_SSL("mail.mclainonline.com", port, context=context) as server:
    server.login("pythontest@mclainonline.com", password)
    sender_email = "pythontest@mclainonline.com"
    to_email = "pdxadam@gmail.com"
    message = """
        Hi Adam, 
        This week we want to go to the Zoo. Will you join us?"""
    msg = EmailMessage()
    msg.set_content("Would you join us in our test survey? You said you would.")
    msg['Subject'] = "Messaging Test Results"
    msg['From'] = sender_email
    msg['To'] = "pythontest@mclainonline.com"
    server.send_message(msg)

