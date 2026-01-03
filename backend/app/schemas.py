# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, field_validator  # Complete V2 import
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

# max_length=72 to prevent bcrypt error
class UserCreate(UserBase):
    password: str
    
    @field_validator('password')
    @classmethod
    def check_password_bytes(cls, v):
        if len(v.encode('utf-8')) > 72:
            raise ValueError('Password exceeds 72 bytes')
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(max_length=100)

class UserOut(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
