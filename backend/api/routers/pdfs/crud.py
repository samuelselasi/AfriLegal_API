#!/usr/bin/python3
"""Module that defines CRUD functions"""

from . import models, schemas
from sqlalchemy.orm import Session


def get_pdf_id(db: Session, pdf_id: int):
    """Function to retrieve pdf based on its id"""

    return db.query(models.PDFDocument).filter(models.PDFDocument.id ==
                                               pdf_id).first()


def get_pdf_title(db: Session, pdf_title: str):
    """Function to retrieve pdf based on title"""

    return db.query(models.PDFDocument).filter(models.PDFDocument.title ==
                                               pdf_title).first()


def create_pdf(db: Session, pdf: schemas.PDFCreate):
    db_pdf = models.PDFDocument(**pdf.dict())
    db.add(db_pdf)
    db.commit()
    db.refresh(db_pdf)
    return db_pdf
