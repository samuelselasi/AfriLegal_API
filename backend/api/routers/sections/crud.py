#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_section(db: Session, section_id: int):
    """Function to read a section based on its id"""

    return db.query(models.Section).filter(models.Section.id ==
                                           section_id).first()


def get_sections_by_country(db: Session, country_id: int,
                            skip: int = 0, limit: int = 100):
    """Function to read section based on country"""

    return db.query(models.Section).filter(models.Section.country_id ==
                                           country_id).offset(
                                                   skip).limit(limit).all()


def get_sections_by_country_and_chapter(db: Session,
                                        country_id: int,
                                        chapter_id: int,
                                        skip: int = 0,
                                        limit: int = 100):
    """Function to read section based on country and chapter"""

    return db.query(models.Section).filter(models.Section.country_id ==
                                           country_id,
                                           models.Section.chapter_id ==
                                           chapter_id).offset(
                                                   skip).limit(limit).all()


def get_sections_by_country_and_chapter_and_article(db: Session,
                                                    country_id: int,
                                                    chapter_id: int,
                                                    article_id: int,
                                                    skip: int = 0,
                                                    limit: int = 100):
    """Function to read section based on country, chapter and article"""

    return db.query(models.Section).filter(models.Section.country_id ==
                                           country_id,
                                           models.Section.chapter_id ==
                                           chapter_id,
                                           models.Section.article_id ==
                                           article_id).offset(
                                                   skip).limit(limit).all()


def create_section(db: Session, section: schemas.SectionCreate,
                   country_id: int, chapter_id: int, article_id: int):
    """Function to create a section for country based on chapter & article"""

    db_section = models.Section(**section.dict(), country_id=country_id,
                                chapter_id=chapter_id, article_id=article_id)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def update_section(db: Session, section_id: int,
                   section_update: schemas.SectionBase):
    """Function to update a section based on its id"""

    db_section = get_section(db, section_id=section_id)
    if db_section:
        for key, value in section_update.dict().items():
            setattr(db_section, key, value)
        db.commit()
        db.refresh(db_section)
        return db_section
    else:
        raise HTTPException(status_code=404, detail="Section not found")


def delete_section(db: Session, section_id: int):
    """Function to delete a section based on its id"""

    db_section = get_section(db, section_id=section_id)
    if db_section:
        db.delete(db_section)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Section not found")
