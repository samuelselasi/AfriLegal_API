#!/usr/bin/python3
"""Module that defines endpoints for chapters"""

from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chapters/", response_model=schemas.Chapter)
async def create_chapter_for_country(country_id: int,
                                     chapter: schemas.ChapterCreate,
                                     db: Session = Depends(get_db)):
    """Endpoint to create a chapter for a country"""

    return crud.create_chapter(db=db, chapter=chapter, country_id=country_id)


@router.get("/chapters/", response_model=List[schemas.Chapter])
async def read_chapters_by_country(country_id: int,
                                   skip: int = 0,
                                   limit: int = 100,
                                   db: Session = Depends(get_db)):
    """Endpoint to get chapters based on country_id"""

    chapters = crud.get_chapters_by_country(db,
                                            country_id=country_id,
                                            skip=skip, limit=limit)
    return chapters


@router.get("/chapters/{chapter_id}", response_model=schemas.Chapter)
async def read_chapter(chapter_id: int, db: Session = Depends(get_db)):
    """Endpoint to get chapetr based on id"""

    db_chapter = crud.get_chapter(db, chapter_id=chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return db_chapter


@router.put("/chapters/{chapter_id}", response_model=schemas.Chapter)
async def update_chapter(chapter_id: int,
                         chapter_update: schemas.ChapterBase,
                         db: Session = Depends(get_db)):
    """Endpoint to update a chapter by id"""

    return crud.update_chapter(db, chapter_id, chapter_update)


@router.delete("/chapters/{chapter_id}", response_model=None)
async def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete a chapter by id"""

    crud.delete_chapter(db, chapter_id)
    return {"message": "Chapter deleted successfully"}
