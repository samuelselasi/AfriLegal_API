#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models
from sqlalchemy.orm import Session


def search_sections_by_keyword(db: Session, country_id: int, keyword: str,
                               skip: int = 0, limit: int = 100):
    """Function to search specific section of a constitution with keyword"""

    return db.query(models.Section).filter(
            models.Section.country_id == country_id,
            models.Section.text.ilike(f'%{keyword}%')).offset(
                    skip).limit(limit).all()


def search_subsections_by_keyword(db: Session, country_id: int, keyword: str,
                                  skip: int = 0, limit: int = 100):
    """Function to search specific subsection of a constitution w/ keyword"""

    return db.query(models.Subsection).filter(
            models.Subsection.country_id == country_id,
            models.Subsection.text.ilike(f'%{keyword}%')).offset(
                    skip).limit(limit).all()


def search_chapters_by_keyword(db: Session, country_id: int, keyword: str,
                               skip: int = 0, limit: int = 100):
    """Function to search specific chapter of a constitution with keyword"""

    return db.query(models.Chapter).filter(
            models.Chapter.country_id == country_id,
            models.Chapter.text.ilike(f'%{keyword}%')).offset(
                    skip).limit(limit).all()


def search_articles_by_keyword(db: Session, country_id: int, keyword: str,
                               skip: int = 0, limit: int = 100):
    """Function to search specific article of a constitution with keyword"""

    return db.query(models.Article).filter(
            models.Article.country_id == country_id,
            models.Article.title.ilike(f'%{keyword}%')).offset(
                    skip).limit(limit).all()
