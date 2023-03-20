import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(to: str, subject: str, message: str, file: bytes = None) -> None:
    msg = MIMEMultipart()
    msg['From'] = 'pratayeu@yandex.ru'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    if file:
        part = MIMEApplication(file, Name='img.png')
        part['Content-Disposition'] = 'attachment; filename="img.png"'
        msg.attach(part)
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pratayeu@yandex.ru', 'tkpldypazgcrqcen')
    server.sendmail('pratayeu@yandex.ru', to, msg.as_string())
