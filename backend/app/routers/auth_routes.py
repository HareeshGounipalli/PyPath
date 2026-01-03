# app/routers/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database, crud, auth

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Dependency to get DB session
get_db = database.get_db

# ---------- REGISTER ----------
# app/routers/auth_routes.py

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    try:
        created_user = crud.create_user(db, user)
        return created_user
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


# ---------- LOGIN ----------
@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):  # Fix: database.get_db
    db_user = crud.get_user_by_email(db, user.email)  # Fix: user.email
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = auth.create_access_token({"sub": str(db_user.id)})  # Fix: db_user.id
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserOut)
def get_me(current_user = Depends(auth.get_current_user)):
    return current_user