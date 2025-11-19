import smtplib, ssl
from getpass import getpass
from email.message import EmailMessage

port = 465
server = "mail.mclainonline.com"
usename = "student"
password = getpass("enter your password")

context = ssl._create_unverified_context()

with smtplib.SMTP_SSL("box2213.bluehost.com", port, context=context) as server:
    server.ehlo()
    server.login("pythontest@mclainonline.com", password)
    server.ehlo()
    sender_email = "pythontest@mclainonline.com"
    to_email = "amclain@riverdale.k12.or.us"
    message = """
        Hi Adam, 
        This week we want to go to the Zoo. Will you join us?"""
    msg = EmailMessage()
    msg.set_content("Would you join us in our test survey? You said you would.")
    msg['Subject'] = "Messaging Test Results"
    msg['From'] = sender_email
    msg['To'] = to_email
    try:
        server.send_message(msg)
    except Exception as e:
        print(f'Error: {e}')

