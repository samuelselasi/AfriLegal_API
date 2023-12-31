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


@router.put("/countries/{country_id}", response_model=schemas.Country)
async def update_country(country_id: int, country_update: schemas.CountryBase, db: Session = Depends(get_db)):
    return crud.update_country(db, country_id, country_update)


@router.delete("/countries/{country_id}", response_model=None)
async def delete_country(country_id: int, db: Session = Depends(get_db)):
    crud.delete_country(db, country_id)
    return {"message": "Country deleted successfully"}
