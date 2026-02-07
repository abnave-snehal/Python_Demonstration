import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
    msg=EmailMessage()

    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject

    msg.set_content(body)

    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)

    smtp.quit()


def main():
    send_email="aalegaonkar712@gmail.com"

    app_password="usqf hulf ncfd zicl"

    receiver_mail="abnave712@gmail.com"

    subject="Test mail from python script"

    body = """Jay Ganesh...

This is a test email sent using Python Script.

Regards,
Snehal Abnave
"""

    send_mail(send_email,app_password,receiver_mail,subject,body)

print("Mail sent successfullt!!!")


if __name__ == "__main__":
    main()
