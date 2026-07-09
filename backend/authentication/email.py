import smtplib
from email.message import EmailMessage
from core.config import settings
import os

def send_verification_email(email: str, token: str):
    verify_url = f"http://localhost:8000/api/auth/verify/{token}"

    print(os.getenv("HOST_EMAIL"))
    print(os.getenv("HOST_PASSWORD"))
    
    msg = EmailMessage()
    msg["Subject"] = "Verify your account"
    msg["From"] = "manahilnoorlcwu@gmail.com"
    msg["To"] = email
    msg.set_content(f"Click to verify: {verify_url}")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(settings.HOST_EMAIL, settings.HOST_PASSWORD)
        server.send_message(msg)
        
    print("Sending email to:", email)

