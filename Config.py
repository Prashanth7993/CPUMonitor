import os

CPU_THRESHOLD = 60  # CPU usage threshold

# Email Configurations
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "jprashanth429@gmail.com")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "jprashanth429@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
