from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from datetime import datetime

# -------------------- Users --------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def check_password_length(cls, v):
        if len(v.encode()) > 72:
            raise ValueError("Password exceeds 72 bytes")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

# -------------------- Auth --------------------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ChangePassword(BaseModel):
    current_password: str
    new_password: str

# -------------------- Lessons --------------------
class LessonBase(BaseModel):
    title: str
    content: str

class LessonOut(LessonBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# -------------------- Tutorials --------------------
class TutorialBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None

class TutorialCreate(TutorialBase):
    lessons: Optional[List[LessonBase]] = []

class TutorialOut(TutorialBase):
    id: int
    created_at: datetime
    lessons: List[LessonOut] = []

    class Config:
        from_attributes = True
