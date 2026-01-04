from sqlalchemy.orm import Session
from . import models, schemas

def create_tutorial(db: Session, tutorial: schemas.TutorialCreate):
    db_tutorial = models.Tutorial(
        title=tutorial.title,
        description=tutorial.description,
        content=tutorial.content
    )
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

def get_tutorials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()

def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()

def update_tutorial(db: Session, tutorial_id: int, tutorial: schemas.TutorialCreate):
    db_tutorial = get_tutorial(db, tutorial_id)
    if not db_tutorial:
        return None
    db_tutorial.title = tutorial.title
    db_tutorial.description = tutorial.description
    db_tutorial.content = tutorial.content
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

def delete_tutorial(db: Session, tutorial_id: int):
    db_tutorial = get_tutorial(db, tutorial_id)
    if not db_tutorial:
        return None
    db.delete(db_tutorial)
    db.commit()
    return db_tutorial

