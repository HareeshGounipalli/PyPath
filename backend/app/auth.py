# app/auth.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import models, database

# =========================
# CONFIG
# =========================
SECRET_KEY = "mL4G8W2-3sDF9vXkqR0pQz7hJt5yN1eB"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")  # No 72-byte 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# =========================
# PASSWORD FUNCTIONS
# =========================
def get_password_hash(password: str) -> str:
    # truncate to 72 chars for bcrypt
    truncated = password[:72]
    return pwd_context.hash(truncated)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password[:72]
    return pwd_context.verify(truncated, hashed_password)

# =========================
# JWT FUNCTIONS
# =========================
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception()
        return payload
    except JWTError:
        raise credentials_exception()

def credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

# =========================
# DATABASE / USER HELPERS
# =========================
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

# =========================
# DEPENDENCY FOR ROUTES
# =========================
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    payload = verify_token(token)
    user_id_str = payload.get("sub")
    if not user_id_str:
        raise credentials_exception()
    try:
        user_id = int(user_id_str)
    except ValueError:
        raise credentials_exception()
    
    user = db.query(models.User).filter(models.User.id == user_id).first()  # Now db available
    if not user:
        raise credentials_exception()
    return user
