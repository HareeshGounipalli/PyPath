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

@router.put("/me", response_model=schemas.UserOut)
def update_profile(
    updated_user: schemas.UserBase,
    current_user=Depends(auth.get_current_user),
    db: Session = Depends(database.get_db)
):
    # Check if email is already used by someone else
    existing_user = crud.get_user_by_email(db, updated_user.email)
    if existing_user and existing_user.id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Update fields
    current_user.name = updated_user.name
    current_user.email = updated_user.email

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user


@router.put("/change-password")
def change_password(
    passwords: schemas.ChangePassword,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(database.get_db)
):
    # Verify current password
    if not auth.verify_password(passwords.current_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Current password is incorrect"
        )
    
    # Hash new password
    current_user.hashed_password = auth.get_password_hash(passwords.new_password)
    db.add(current_user)
    db.commit()
    return {"message": "Password updated successfully"}
