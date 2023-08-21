"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_chapter(db: Session, chapter_id: int):
    return db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()

def get_chapters_by_country(db: Session, country_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Chapter).filter(models.Chapter.country_id == country_id).offset(skip).limit(limit).all()

def create_chapter(db: Session, chapter: schemas.ChapterCreate, country_id: int):
    db_chapter = models.Chapter(**chapter.dict(), country_id=country_id)
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter

def update_chapter(db: Session, chapter_id: int, chapter_update: schemas.ChapterBase):
    db_chapter = get_chapter(db, chapter_id=chapter_id)
    if db_chapter:
        for key, value in chapter_update.dict().items():
            setattr(db_chapter, key, value)
        db.commit()
        db.refresh(db_chapter)
        return db_chapter
    else:
        raise HTTPException(status_code=404, detail="Chapter not found")


def delete_chapter(db: Session, chapter_id: int):
    db_chapter = get_chapter(db, chapter_id=chapter_id)
    if db_chapter:
        db.delete(db_chapter)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Chapter not found")
