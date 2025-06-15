import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()


def login(email, password):
    server.starttls()
    server.login(email, password)


def send_email(email, from_field, to_field, subject_field, message_filename, attachment_path):
    email_msg = MIMEMultipart()
    email_msg['From'] = from_field
    email_msg['To'] = to_field
    email_msg['Subject'] = subject_field

    with open(message_filename, 'r') as f:
        message = f.read()
    email_msg.attach(MIMEText(message, 'plain'))

    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        'Content-Disposition',
        f'attachment; filename="{attachment_path.split("/")[-1]}"',
    )

    email_msg.attach(part)

    text = email_msg.as_string()
    server.sendmail(email, to_field, text)