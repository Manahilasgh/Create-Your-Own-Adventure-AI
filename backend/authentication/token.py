from itsdangerous import URLSafeTimedSerializer

serializer = URLSafeTimedSerializer("email-secret")

def generate_verification_token(email: str):
    return serializer.dumps(email)

def verify_verification_token(token: str, max_age=3600):
    return serializer.loads(token, max_age=max_age)
