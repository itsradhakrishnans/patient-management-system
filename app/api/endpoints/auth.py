from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps

router = APIRouter()

@router.post("/signup", response_model=schemas.User)
def signup(user_in: schemas.user.UserCreate, db: Session = Depends(deps.get_db)):
    user = db.query(models.User).filter(models.User.username == user_in.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = deps.get_password_hash(user_in.password)
    user = models.User(username=user_in.username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(user_in: schemas.user.UserCreate, db: Session = Depends(deps.get_db)):
    user = db.query(models.User).filter(models.User.username == user_in.username).first()
    if not user or not deps.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = deps.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
