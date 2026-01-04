# app/routers/tutorial_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas, auth

router = APIRouter(
    prefix="/tutorials",
    tags=["Tutorials"]
)

@router.get("/")
def get_all_tutorials(db: Session = Depends(database.get_db)):
    return db.query(models.Tutorial).all()

