# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas, auth
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Hash password with truncation
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        role="student"  # default role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_tutorial(db: Session, tutorial: schemas.TutorialCreate):
    db_tutorial = models.Tutorial(title=tutorial.title, description=tutorial.description)
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)

    # Add lessons if any
    for lesson in tutorial.lessons:
        db_lesson = models.Lesson(
            title=lesson.title,
            content=lesson.content,
            tutorial_id=db_tutorial.id
        )
        db.add(db_lesson)
    db.commit()
    return db_tutorial

def get_tutorials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()

def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()