import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Environment variables for email
# sender_email = os.getenv("MAIL_SENDER", "include_email_sender_here")
# receiver_email = os.getenv("MAIL_RECEIVER", "put_email_receiver_here")
# password = os.getenv("MAIL_APP_PASSWORD", "put_mail_app_pass_here")

# Ngrok or hosted Laravel page URL
WEBPAGE_URL = "https://localhost:8000/birthday"

# Create the MIMEMultipart message
msg = MIMEMultipart("alternative")
msg["Subject"] = "🎉 Birthday Surprise! 🎉"
msg["From"] = sender_email
msg["To"] = receiver_email

# HTML Email
html = f"""
<html>
  <body style="text-align:center; font-family: Arial, sans-serif;">
    <h2>🎉 Happy Birthday! 🎉</h2>
    <img src="https://i.ibb.co/8cQm9Vv/birthday-cake.png" alt="Birthday Image" width="300">
    <p style="font-size:16px; margin-top:20px;">
        Claim it here: 
        <a href="{WEBPAGE_URL}" style="color:#ffffff; background-color:#f39c12; 
           padding:10px 20px; text-decoration:none; border-radius:5px;">
            Click Me!
        </a>
    </p>
  </body>
</html>
"""

# Attach HTML to email
msg.attach(MIMEText(html, "html"))

# Send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully!")
