import smtplib
from email.mime.text import MIMEText
from decrypt_password import decrypt_password
from Config import EMAIL_SENDER, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT

def send_email(process_name, cpu_usage):
    """ Send email alert when a system process exceeds CPU usage. """
    password = decrypt_password()

    subject = "⚠️ High CPU Usage Alert"
    body = f"System process '{process_name}' is consuming {cpu_usage}% CPU. Immediate action required."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        print("📨 Sending email alert...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, password)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
