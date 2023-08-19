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


@router.post("/articles/", response_model=schemas.Article)
async def create_article_for_country_and_chapter(
    country_id: int, chapter_id: int, article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article, country_id=country_id, chapter_id=chapter_id)

@router.get("/articles/", response_model=List[schemas.Article])
async def read_articles_by_country_and_chapter(
    country_id: int, chapter_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles_by_country_and_chapter(db, country_id=country_id, chapter_id=chapter_id, skip=skip, limit=limit)
    return articles

@router.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article
