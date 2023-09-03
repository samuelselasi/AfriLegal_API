#!/usr/bin/python3
"""Module that defines endpoints for items"""

from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import Depends, HTTPException, APIRouter

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate,
                      db: Session = Depends(get_db)):
    """Endpoint to create a user"""

    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
                status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100,
                     db: Session = Depends(get_db)):
    """Edpoint to read all users"""

    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    """Endpoint to read user by id"""

    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
