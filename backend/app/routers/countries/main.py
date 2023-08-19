from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/regions/{region_id}/country/", response_model=schemas.Country)
async def create_country_for_region(
    region_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_region_country(db=db, country=country, region_id=region_id)


@router.get("/countries/", response_model=List[schemas.Country])
async def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries
