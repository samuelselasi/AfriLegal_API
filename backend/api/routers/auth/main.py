#!/usr/bin/python3
"""Module that defines endpoints for articles"""

from typing import List
from fastapi import Depends, HTTPException, BackgroundTasks, APIRouter
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from api.oauth2 import oauth2_scheme

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=schemas.User)
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return await crud.get_current_user(token, db)


# USER LOGIN/LOGOUT
@router.post("/login", description="authenticate user details", response_model=schemas.AuthResponse)
async def authenticate(payload: schemas.Auth, db: Session = Depends(get_db)):
    return await crud.authenticate(payload, db)


@router.post("/logout", description="revoke token")
async def logout(payload: schemas.Token, db: Session = Depends(get_db)):
    return await crud.revoke_token(payload, db)


# REFRESH ACCESS TOKEN
@router.post("/refresh", description="refresh user access/refresh tokens", response_model=schemas.Token)
async def refresh_token(payload: schemas.Token, db: Session = Depends(get_db)):
    return await crud.refresh_token(payload, db)


# RESET PASSWORD
@router.post("/request", description="authenticate user details")
async def request_password_reset(payload: schemas.UserBase, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    return await crud.request_password_reset_(payload, db, background_tasks)
