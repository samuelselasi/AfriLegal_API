from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
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


@router.post("/sections/", response_model=schemas.Section)
async def create_section_for_country_chapter_article(
    country_id: int, chapter_id: int, article_id: int, section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db=db, section=section, country_id=country_id, chapter_id=chapter_id, article_id=article_id)

@router.get("/sections/", response_model=List[schemas.Section])
async def read_sections_by_country_chapter_article(
    country_id: int, chapter_id: int, article_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections_by_country_and_chapter_and_article(db, country_id=country_id, chapter_id=chapter_id, article_id=article_id, skip=skip, limit=limit)
    return sections

@router.get("/sections/{section_id}", response_model=schemas.Section)
async def read_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section
