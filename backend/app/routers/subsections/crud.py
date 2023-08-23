"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_subsection(db: Session, subsection_id: int):
    return db.query(models.Subsection).filter(models.Subsection.id == subsection_id).first()

def get_subsections_by_country_and_chapter_and_article_and_section(db: Session, country_id: int, chapter_id: int, article_id: int, section_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Subsection).filter(models.Subsection.country_id == country_id, models.Subsection.chapter_id == chapter_id, models.Subsection.article_id == article_id, models.Subsection.section_id == section_id).offset(skip).limit(limit).all()

def create_subsection(db: Session, subsection: schemas.SubsectionCreate, country_id: int, chapter_id: int, article_id: int, section_id: int):
    db_subsection = models.Subsection(**subsection.dict(), country_id=country_id, chapter_id=chapter_id, article_id=article_id, section_id=section_id)
    db.add(db_subsection)
    db.commit()
    db.refresh(db_subsection)
    return db_subsection


def update_subsection(db: Session, subsection_id: int, subsection_update: schemas.SubsectionBase):
    db_subsection = get_subsection(db, subsection_id=subsection_id)
    if db_subsection:
        for key, value in subsection_update.dict().items():
            setattr(db_subsection, key, value)
        db.commit()
        db.refresh(db_subsection)
        return db_subsection
    else:
        raise HTTPException(status_code=404, detail="Subsection not found")

def delete_subsection(db: Session, subsection_id: int):
    db_subsection = get_subsection(db, subsection_id=subsection_id)
    if db_subsection:
        db.delete(db_subsection)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Subsection not found")
