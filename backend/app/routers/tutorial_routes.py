from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database, models, auth
from typing import List

router = APIRouter(
    prefix="/tutorials",
    tags=["Tutorials"]
)

# -------------------- Create tutorial --------------------
@router.post("/", response_model=schemas.TutorialOut)
def create_tutorial(tutorial: schemas.TutorialCreate, 
                    db: Session = Depends(database.get_db),
                    current_user: models.User = Depends(auth.get_current_user)):
    db_tutorial = models.Tutorial(
        title=tutorial.title,
        description=tutorial.description,
        category=tutorial.category
    )
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)

    for lesson in tutorial.lessons:
        db_lesson = models.Lesson(
            title=lesson.title,
            content=lesson.content,
            tutorial_id=db_tutorial.id
        )
        db.add(db_lesson)
    db.commit()
    return db_tutorial

# -------------------- List tutorials --------------------
@router.get("/", response_model=List[schemas.TutorialOut])
def list_tutorials(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()

# -------------------- Get tutorial detail --------------------
@router.get("/{tutorial_id}", response_model=schemas.TutorialOut)
def get_tutorial(tutorial_id: int, db: Session = Depends(database.get_db)):
    tutorial = db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return tutorial

# -------------------- Add lesson --------------------
@router.post("/{tutorial_id}/lessons", response_model=schemas.LessonOut)
def add_lesson(tutorial_id: int,
               lesson: schemas.LessonBase,
               db: Session = Depends(database.get_db),
               current_user: models.User = Depends(auth.get_current_user)):
    tutorial = db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")

    db_lesson = models.Lesson(
        title=lesson.title,
        content=lesson.content,
        tutorial_id=tutorial_id
    )
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson
