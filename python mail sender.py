from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'your-email@gmail.com'
email_password = 'your-app-password'
email_receiver = 'receiver-email@example.com'

subject = 'Test Email'
body = """
This is a test email sent from a Python script.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
