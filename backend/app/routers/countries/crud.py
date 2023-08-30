"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def create_region_country(db: Session, country: schemas.CountryCreate, region_id: int):
    db_country = models.Country(**country.dict(), region_id=region_id)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


def update_country(db: Session, country_id: int, country_update: schemas.CountryBase):
    db_country = get_country(db, country_id=country_id)
    if db_country:
        for key, value in country_update.dict().items():
            setattr(db_country, key, value)
        db.commit()
        db.refresh(db_country)
        return db_country
    else:
        raise HTTPException(status_code=404, detail="Country not found")


def delete_country(db: Session, country_id: int):
    db_country = get_country(db, country_id=country_id)
    if db_country:
        db.delete(db_country)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Country not found")
