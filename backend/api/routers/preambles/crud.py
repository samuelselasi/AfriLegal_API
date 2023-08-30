"""Module that defines CRUD functions"""

from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_preamble(db: Session, preamble_id: int):
    """Function to get preamble based on its id"""

    return db.query(models.Preamble).filter(models.Preamble.id ==
                                            preamble_id).first()


def get_preambles_by_country(db: Session, country_id: int, skip: int = 0,
                             limit: int = 100):
    """Function to get preamble based on country id"""

    return db.query(models.Preamble).filter(models.Preamble.country_id ==
                                            country_id).offset(skip).limit(
                                                    limit).all()


def create_preamble(db: Session, preamble: schemas.PreambleCreate,
                    country_id: int):
    """Function to create preamble for a country"""

    db_preamble = models.Preamble(**preamble.dict(), country_id=country_id)
    db.add(db_preamble)
    db.commit()
    db.refresh(db_preamble)
    return db_preamble


def update_preamble(db: Session, preamble_id: int,
                    preamble_update: schemas.PreambleBase):
    """Function to update preamble of a country based on its id"""

    db_preamble = get_preamble(db, preamble_id=preamble_id)
    if db_preamble:
        for key, value in preamble_update.dict().items():
            setattr(db_preamble, key, value)
        db.commit()
        db.refresh(db_preamble)
        return db_preamble
    else:
        raise HTTPException(status_code=404, detail="Preamble not found")


def delete_preamble(db: Session, preamble_id: int):
    """Funtion to delete preamble based on its id"""

    db_preamble = get_preamble(db, preamble_id=preamble_id)
    if db_preamble:
        db.delete(db_preamble)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Preamble not found")
