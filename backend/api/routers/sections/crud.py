"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_section(db: Session, section_id: int):
    return db.query(models.Section).filter(models.Section.id == section_id).first()

def get_sections_by_country_and_chapter_and_article(db: Session, country_id: int, chapter_id: int, article_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Section).filter(models.Section.country_id == country_id, models.Section.chapter_id == chapter_id, models.Section.article_id == article_id).offset(skip).limit(limit).all()

def create_section(db: Session, section: schemas.SectionCreate, country_id: int, chapter_id: int, article_id: int):
    db_section = models.Section(**section.dict(), country_id=country_id, chapter_id=chapter_id, article_id=article_id)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


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
