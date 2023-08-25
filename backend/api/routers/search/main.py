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


@router.get("/search/sections/", response_model=List[schemas.Section])
async def search_sections_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    sections = crud.search_sections_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return sections

@router.get("/search/subsections/", response_model=List[schemas.Subsection])
async def search_subsections_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    subsections = crud.search_subsections_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return subsections

@router.get("/search/chapters/", response_model=List[schemas.Chapter])
async def search_chapters_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    chapters = crud.search_chapters_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return chapters


@router.get("/search/articles/", response_model=List[schemas.Article])
async def search_articles_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    articles = crud.search_articles_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return articles
