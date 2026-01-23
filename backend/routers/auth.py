from fastapi import APIRouter, HTTPException, Depends
from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from models.user import User
from authentication.password import verify_password, hash_password
from authentication.email import send_verification_email
from authentication.token import generate_verification_token, verify_verification_token
from authentication.jwt import create_access_token
from schemas.userSignUp import UserSignup
from schemas.userLogin import UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/signup")
def signup(data: UserSignup, db: Session = Depends(get_db)):
    user = User(
        username = data.username,
        email = data.email,
        hash_password = hash_password(data.password),
        isVerified = False
    )
    db.add(user)
    db.commit()

    token = generate_verification_token(data.email)
    send_verification_email(data.email, token)

    return {"message": "check your email to verify", "token": token}

@router.get("/verify")
def verify_email(token: str, db: Session = Depends(get_db)):
    email = verify_verification_token(token)

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.isVerified = True
    db.commit()

    return {"message": "User verified"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.hash_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    if not user.isVerified:
        raise HTTPException(status_code=403, detail="User not verified")

    token = create_access_token({"sub": user.email})
    return {"access_token": token}





