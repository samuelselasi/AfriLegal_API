"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_region(db: Session, region_id: int):
    return db.query(models.Region).filter(models.Region.id == region_id).first()


def get_region_by_name(db: Session, name: str):
    return db.query(models.Region).filter(models.Region.name == name).first()


def get_regions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Region).offset(skip).limit(limit).all()


def create_region(db: Session, region: schemas.RegionCreate):
    db_region = models.Region(name=region.name)
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def create_region_country(db: Session, country: schemas.CountryCreate, region_id: int):
    db_country = models.Country(**country.dict(), region_id=region_id)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


def update_region(db: Session, region_id: int, region_update: schemas.RegionBase):
    db_region = get_region(db, region_id=region_id)
    if db_region:
        for key, value in region_update.dict().items():
            setattr(db_region, key, value)
        db.commit()
        db.refresh(db_region)
        return db_region
    else:
        raise HTTPException(status_code=404, detail="Region not found")


def delete_region(db: Session, region_id: int):
    db_region = get_region(db, region_id=region_id)
    if db_region:
        db.delete(db_region)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Region not found")
