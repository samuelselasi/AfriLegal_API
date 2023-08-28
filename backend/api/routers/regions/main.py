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


@router.get("/get_regions", response_model=List[schemas.Region])
async def read_regions(skip: int = 0,
                       limit: int = 100,
                       db: Session = Depends(get_db)):
    """Endpooint to read all regions"""

    regions = crud.get_regions(db, skip=skip, limit=limit)
    return regions


@router.get("/get_region/{region_id}", response_model=schemas.Region)
async def read_region(region_id: int, db: Session = Depends(get_db)):
    """Endpoint to read region based on its id"""

    db_region = crud.get_region(db, region_id=region_id)
    if db_region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    return db_region


@router.post("/create_region", response_model=schemas.Region)
async def create_region(region: schemas.RegionCreate,
                        db: Session = Depends(get_db)):
    """Endpoint to create a region"""

    db_region = crud.get_region_by_name(db, name=region.name)
    if db_region:
        raise HTTPException(status_code=400,
                            detail="Name already registered")
    return crud.create_region(db=db, region=region)


# @router.post("/create_country/{region_id}", response_model=schemas.Country)
async def create_country_for_region(region_id: int,
                                    country: schemas.CountryCreate,
                                    db: Session = Depends(get_db)):
    """Endpoint to create country based on region_id"""

    return crud.create_region_country(db=db, country=country, region_id=region_id)


@router.put("/update_region/{region_id}", response_model=schemas.Region)
async def update_region(region_id: int,
                        region_update: schemas.RegionBase,
                        db: Session = Depends(get_db)):
    """Endpoint to update region based on its id"""

    return crud.update_region(db, region_id, region_update)


@router.delete("/delete_region/{region_id}", response_model=None)
async def delete_region(region_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete region based on its id"""

    crud.delete_region(db, region_id)
    return {"message": "Region deleted successfully"}
