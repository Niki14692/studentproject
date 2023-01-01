import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "niku17patel@gmail.com"
    password = os.getenv("PASSWORD")


    receiver = "niku17patel@gmail.com"

    context =ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



