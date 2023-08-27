from typing import List

from fastapi import Depends, APIRouter
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


@router.get("/search/chapters/", response_model=List[schemas.Chapter])
async def search_chapters_by_keyword(country_id: int,
                                     keyword: str,
                                     skip: int = 0,
                                     limit: int = 100,
                                     db: Session = Depends(get_db)):
    """Endpoint to read chapters based on country_id and keywords"""

    chapters = crud.search_chapters_by_keyword(db,
                                               country_id=country_id,
                                               keyword=keyword,
                                               skip=skip,
                                               limit=limit)
    return chapters


@router.get("/search/articles/", response_model=List[schemas.Article])
async def search_articles_by_keyword(country_id: int,
                                     keyword: str,
                                     skip: int = 0,
                                     limit: int = 100,
                                     db: Session = Depends(get_db)):
    """Endpoint to read articles based on country_id and keywords"""

    articles = crud.search_articles_by_keyword(db,
                                               country_id=country_id,
                                               keyword=keyword,
                                               skip=skip,
                                               limit=limit)
    return articles


@router.get("/search/sections/", response_model=List[schemas.Section])
async def search_sections_by_keyword(country_id: int,
                                     keyword: str,
                                     skip: int = 0,
                                     limit: int = 100,
                                     db: Session = Depends(get_db)):
    """Endpoint to read sections based on country_id and keywords"""

    sections = crud.search_sections_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit)
    return sections


@router.get("/search/subsections/", response_model=List[schemas.Subsection])
async def search_subsections_by_keyword(country_id: int,
                                        keyword: str,
                                        skip: int = 0,
                                        limit: int = 100,
                                        db: Session = Depends(get_db)):
    """Endpoint to read subsections based on country_id and keywords"""

    subsections = crud.search_subsections_by_keyword(db,
                                                     country_id=country_id,
                                                     keyword=keyword,
                                                     skip=skip,
                                                     limit=limit)
    return subsections
