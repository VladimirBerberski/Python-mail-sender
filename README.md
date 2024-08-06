# Python-mail-sender by Vladimir Berberski
Python script that sends emails using Google SMTP

First you need to create Google App Password

1.Sign in to Your Google Account:
Go to myaccount.google.com and log in with your credentials.


2.Navigate to Security:
In the left-hand menu, select "Security."

3.Enable 2-Step Verification:
Under "Signing in to Google," make sure 2-Step Verification is turned on. If not, follow the prompts to enable it.

4.Generate an App Password:
After enabling 2-Step Verification, scroll down and find the "App passwords" section. Click on it.
You may be asked to re-enter your Google password.
Click "Select app" and choose the app you're generating the password for, or select "Other (Custom name)" to enter a specific name.
Click "Generate."

5.Use the Generated Password:
A 16-character password will be displayed. Use this password in the app instead of your regular Google account password.

Now for the code 
your need to change the contend in : email_sender , email_password , email_receiver , subject , body
email sender = the email you want to send the email from
email_password = the password from google that you generated 
email_receiver = the email or emails that you wand to recive the email
subject = the subject of the email
body = the message in the email 
