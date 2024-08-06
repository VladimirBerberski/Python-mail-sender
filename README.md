Python Mail Sender by Vladimir Berberski
A simple Python script that sends emails using Google SMTP.

Setup Instructions
1. Create a Google App Password
  •Sign in to Your Google Account:
  Go to myaccount.google.com and log in with your credentials.

  •Navigate to Security:
  In the left-hand menu, select "Security."

  •Enable 2-Step Verification:
  Under "Signing in to Google," ensure 2-Step Verification is turned on. Follow the prompts to enable it if it's not already       enabled.

  •Generate an App Password:
  After enabling 2-Step Verification, scroll down to find the "App passwords" section and click on it.
  Re-enter your Google password if prompted.
  Click "Select app" and choose the app you're generating the password for, or select "Other (Custom name)" to specify a name.
  Click "Generate."
  
  •Use the Generated Password:
  A 16-character password will be displayed. Use this password in the script instead of your regular Google account password.

2. Configure the Script
Replace the placeholder values in the script with your specific details:

email_sender: Your Gmail address.
email_password: The App Password you generated.
email_receiver: The recipient's email address. For multiple recipients, separate them with commas.
subject: The subject of the email.
body: The body text of the email.


Dependencies
Make sure you have the necessary dependencies installed. You can install them using:
pip install secure-smtplib
