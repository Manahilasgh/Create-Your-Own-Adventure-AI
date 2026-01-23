from dns.tsig import HMAC_SHA256_128
from jose import jwt
from datetime import datetime, timedelta

def create_access_token(data: dict, expires_minutes: int = 240):
    ALGORITHM = "HS256"
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=expires_minutes)
    SECRET = "Sfjhk2c9nfj2GioefWLObyyXn9VUkYJU"
    return jwt.encode(payload, SECRET, ALGORITHM)