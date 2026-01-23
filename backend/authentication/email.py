import smtplib
from email.message import EmailMessage
from core.config import settings

def send_verification_email(email: str, token: str):
    verify_url = f"http://localhost:3000/verify-email?token={token}"

    msg = EmailMessage()
    msg["Subject"] = "Verify your account"
    msg["From"] = "manahil.noor@datics.ai"
    msg["To"] = email
    msg.set_content(f"Click to verify: {verify_url}")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(settings.HOST_EMAIL, settings.HOST_PASSWORD)
        server.send_message(msg)

