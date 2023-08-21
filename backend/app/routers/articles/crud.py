"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def get_articles_by_country_and_chapter(db: Session, country_id: int, chapter_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Article).filter(models.Article.country_id == country_id, models.Article.chapter_id == chapter_id).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate, country_id: int, chapter_id: int):
    db_article = models.Article(**article.dict(), country_id=country_id, chapter_id=chapter_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update_article(db: Session, article_id: int, article_update: schemas.ArticleBase):
    db_article = get_article(db, article_id=article_id)
    if db_article:
        for key, value in article_update.dict().items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
        return db_article
    else:
        raise HTTPException(status_code=404, detail="Article not found")

def delete_article(db: Session, article_id: int):
    db_article = get_article(db, article_id=article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Article not found")
