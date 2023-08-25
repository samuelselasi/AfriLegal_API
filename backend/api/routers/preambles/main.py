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


@router.post("/preambles/", response_model=schemas.Preamble)
async def create_preamble_for_country(
    country_id: int, preamble: schemas.PreambleCreate, db: Session = Depends(get_db)):
    return crud.create_preamble(db=db, preamble=preamble, country_id=country_id)

@router.get("/preambles/", response_model=List[schemas.Preamble])
async def read_preambles_by_country(
    country_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    preambles = crud.get_preambles_by_country(db, country_id=country_id, skip=skip, limit=limit)
    return preambles

@router.get("/preambles/{preamble_id}", response_model=schemas.Preamble)
async def read_preamble(preamble_id: int, db: Session = Depends(get_db)):
    db_preamble = crud.get_preamble(db, preamble_id=preamble_id)
    if db_preamble is None:
        raise HTTPException(status_code=404, detail="Preamble not found")
    return db_preamble


@router.put("/preambles/{preamble_id}", response_model=schemas.Preamble)
async def update_preamble(
    preamble_id: int, preamble_update: schemas.PreambleBase, db: Session = Depends(get_db)
):
    return crud.update_preamble(db, preamble_id, preamble_update)


@router.delete("/preambles/{preamble_id}", response_model=None)
async def delete_preamble(preamble_id: int, db: Session = Depends(get_db)):
    crud.delete_preamble(db, preamble_id)
    return {"message": "Preamble deleted successfully"}
