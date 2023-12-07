import smtplib
import ssl
from email.message import EmailMessage

subject = "Sent from python"
body = "This ia an email message from python!!"
sender_email = "dimejiademola5@gmail.com"
receiver_email = "dimejiademola5@gmail.com"
password = input("enter a password: ")

message = EmailMessage()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Email successfully sent")