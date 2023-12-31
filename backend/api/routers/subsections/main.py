#!/usr/bin/python3
"""Module that defines endpoints for articles"""

from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import Depends, HTTPException, APIRouter

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_subsection_by_country/{country_id}",
            response_model=List[schemas.Subsection])
async def read_subsections_by_country(
        country_id: int, skip: int = 0, limit: int = 100,
        db: Session = Depends(get_db)):
    """Endpoint to read subsection based on country id"""

    subsections = crud.get_subsections_by_country(
            db, country_id=country_id, skip=skip, limit=limit)
    return subsections


@router.get("/get_subsection_by_cc/{country_id}/{chapter_id}",
            response_model=List[schemas.Subsection])
async def read_subsections_by_country_and_chapter(
        country_id: int, chapter_id: int, skip: int = 0,
        limit: int = 100, db: Session = Depends(get_db)):
    """Endpoint to read subsection based on country id and chapter id"""

    subsections = crud.get_subsections_by_country_chapter(
            db, country_id=country_id, chapter_id=chapter_id,
            skip=skip, limit=limit)
    return subsections


@router.get("/get_subsection_by_cca/{country_id}/{chapter_id}/{article_id}",
            response_model=List[schemas.Subsection])
async def read_subsections_by_country_chapter_and_article(
        country_id: int, chapter_id: int, article_id: int, skip: int = 0,
        limit: int = 100, db: Session = Depends(get_db)):
    """Endpoint to read subsection based on country, chapter and article"""

    subsections = crud.get_subsections_by_country_chapter_article(
            db, country_id=country_id, chapter_id=chapter_id,
            article_id=article_id, skip=skip, limit=limit)
    return subsections


@router.get("/get_subsection_by_ccas/{country}/{chapter}/{article}/{section}",
            response_model=List[schemas.Subsection])
async def read_subsections_by_country_chapter_article_and_section(
        country_id: int, chapter_id: int, article_id: int, section_id: int,
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Endpoint to read subsection based on country, chapter, article..."""

    subsections = crud.get_subsections_by_country_chapter_article_section(
            db, country_id=country_id, chapter_id=chapter_id,
            article_id=article_id, section_id=section_id,
            skip=skip, limit=limit)
    return subsections


@router.get("/get_subsection/{subsection_id}",
            response_model=schemas.Subsection)
async def read_subsection(subsection_id: int, db: Session = Depends(get_db)):
    """Endpoint to read subsection based on its id"""

    db_subsection = crud.get_subsection(db, subsection_id=subsection_id)
    if db_subsection is None:
        raise HTTPException(status_code=404, detail="Subsection not found")
    return db_subsection


@router.post("/create_subsection/{country}/{chapter}/{article}/{section}",
             response_model=schemas.Subsection)
async def create_subsection(country_id: int,
                            chapter_id: int,
                            article_id: int,
                            section_id: int,
                            subsection: schemas.SubsectionCreate,
                            db: Session = Depends(get_db)):
    """Endpoint to create subsection with country, chapter, article..."""

    return crud.create_subsection(db=db,
                                  subsection=subsection,
                                  country_id=country_id,
                                  chapter_id=chapter_id,
                                  article_id=article_id,
                                  section_id=section_id)


@router.put("/update_subsection/{subsection_id}",
            response_model=schemas.Subsection)
async def update_subsection(subsection_id: int,
                            subsection_update: schemas.SubsectionBase,
                            db: Session = Depends(get_db)):
    """Endpoint to update a subsection based on its id"""

    return crud.update_subsection(db, subsection_id, subsection_update)


@router.delete("/delete_subsection/{subsection_id}", response_model=None)
async def delete_subsection(subsection_id: int,
                            db: Session = Depends(get_db)):
    """Endpoint to delete a subsection based on its id"""

    crud.delete_subsection(db, subsection_id)
    return {"message": "Subsection deleted successfully"}
