#!/usr/bin/python3
"""Module that defines endpoints for articles"""

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


@router.get("/get_articles", response_model=List[schemas.Article])
async def read_articles_by_country_and_chapter(country_id: int,
                                               chapter_id: int,
                                               skip: int = 0,
                                               limit: int = 100,
                                               db: Session = Depends(get_db)):
    """Endpoint to get article based country_id & chapter_id"""

    articles = crud.get_articles_by_country_and_chapter(db,
                                                        country_id=country_id,
                                                        chapter_id=chapter_id,
                                                        skip=skip,
                                                        limit=limit)
    return articles


@router.get("/get_article/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: Session = Depends(get_db)):
    """Endpoint to gret an article based on its id"""

    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@router.post("/create_article/{country_id}/{chapter_id}",
             response_model=schemas.Article)
async def create_article_for_country_and_chapter(country_id: int,
                                                 chapter_id: int,
                                                 article:
                                                 schemas.ArticleCreate,
                                                 db:
                                                 Session = Depends(get_db)):
    """Endpoint to create an article based on country_id and chapter_id"""

    return crud.create_article(db=db, article=article, country_id=country_id,
                               chapter_id=chapter_id)


@router.put("/update_article/{article_id}", response_model=schemas.Article)
async def update_article(article_id: int, article_update: schemas.ArticleBase,
                         db: Session = Depends(get_db)):
    """Endpoint to update an article based on its id"""

    return crud.update_article(db, article_id, article_update)


@router.delete("/delete_article/{article_id}", response_model=None)
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete an article based on its id"""

    crud.delete_article(db, article_id)
    return {"message": "Article deleted successfully"}
