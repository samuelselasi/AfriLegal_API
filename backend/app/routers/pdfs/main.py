#!/usr/bin/python3
"""Module that defines endpoints for articles"""

import io
from typing import List
from fastapi import Depends, HTTPException, APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
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


@router.get("/articles/", response_model=List[schemas.Article])
async def read_articles_by_country_and_chapter(country_id: int,
                                               chapter_id: int,
                                               skip: int = 0,
                                               limit: int = 100,
                                               db: Session = Depends(get_db)):
    """Function that defines endpoint to get article w/ country & chapter"""

    articles = crud.get_articles_by_country_and_chapter(db,
                                                        country_id=country_id,
                                                        chapter_id=chapter_id,
                                                        skip=skip,
                                                        limit=limit)
    return articles


@router.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: Session = Depends(get_db)):
    """Function that defines endpoint to gret an article based on its id"""

    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@router.post("/articles/", response_model=schemas.Article)
async def create_article_for_country_and_chapter(country_id: int,
                                                 chapter_id: int,
                                                 article:
                                                 schemas.ArticleCreate,
                                                 db:
                                                 Session = Depends(get_db)):
    """Function that defines endpoint to create an article"""

    return crud.create_article(db=db, article=article, country_id=country_id,
                               chapter_id=chapter_id)


@router.put("/articles/{article_id}", response_model=schemas.Article)
async def update_article(article_id: int, article_update: schemas.ArticleBase,
                         db: Session = Depends(get_db)):
    """Function that defines endpoint to update an article based on its id"""

    return crud.update_article(db, article_id, article_update)


@router.delete("/articles/{article_id}", response_model=None)
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    """Function that defines endpoint to delete an article based on its id"""

    crud.delete_article(db, article_id)
    return {"message": "Article deleted successfully"}


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...),
                     db: Session = Depends(get_db)):
    """Function that defines endpoint to upload a pdf"""

    pdf_content = file.file.read()
    pdf_data = schemas.PDFCreate(title=file.filename, content=pdf_content)
    db_pdf = crud.create_pdf(db, pdf_data)
    return {"message": "PDF uploaded successfully", "pdf_id": db_pdf.id}


@router.get("/pdf/{pdf_id}/")
async def get_pdf(pdf_id: int, db: Session = Depends(get_db)):
    """Function that defines endpoint to download pdf based on id"""

    pdf = crud.get_pdf(db, pdf_id)
    if pdf:
        return StreamingResponse(io.BytesIO(pdf.content),
                                 media_type="application/pdf")
    return {"message": "PDF not found"}
