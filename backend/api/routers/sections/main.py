from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import Depends, HTTPException, APIRouter

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_section_by_country/{country_id}",
            response_model=List[schemas.Section])
async def read_sections_by_country(country_id: int,
                                   skip: int = 0,
                                   limit: int = 100,
                                   db: Session = Depends(get_db)):
    """Endpoint to read section with country id"""

    sections = crud.get_sections_by_country(db, country_id=country_id,
                                            skip=skip, limit=limit)
    return sections


@router.get("/get_section_by_country_and_chapter/{country_id}/{chapter_id}",
            response_model=List[schemas.Section])
async def read_sections_by_country_and_chapter(country_id: int,
                                               chapter_id: int,
                                               skip: int = 0,
                                               limit: int = 100,
                                               db: Session = Depends(get_db)):
    """Endpoint to read section with country id and chapter id"""

    sections = crud.get_sections_by_country_and_chapter(db,
                                                        country_id=country_id,
                                                        chapter_id=chapter_id,
                                                        skip=skip,
                                                        limit=limit)
    return sections


@router.get("/get_section/{country_id}/{chapter_id}/{article_id}",
            response_model=List[schemas.Section])
async def read_sections_by_country_chapter_article(country_id: int,
                                                   chapter_id: int,
                                                   article_id: int,
                                                   skip: int = 0,
                                                   limit: int = 100,
                                                   db: Session = Depends(
                                                       get_db)):
    """Endpoint to read section with country_id, chapter_id & article_id"""

    s = crud.get_sections_by_country_and_chapter_and_article(
            db, country_id=country_id, chapter_id=chapter_id,
            article_id=article_id, skip=skip, limit=limit)
    return s


@router.get("/read_section/{section_id}", response_model=schemas.Section)
async def read_section(section_id: int, db: Session = Depends(get_db)):
    """Endpoint to read section based on its id"""

    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section


@router.post("/create_section/{country_id}/{chapter_id}/{article_id}",
             response_model=schemas.Section)
async def create_section_for_country_chapter_article(country_id: int,
                                                     chapter_id: int,
                                                     article_id: int,
                                                     section:
                                                     schemas.SectionCreate,
                                                     db:
                                                     Session =
                                                     Depends(get_db)):
    """Endpoint to create section with country_id, chapter_id & article_id"""

    return crud.create_section(db=db,
                               section=section,
                               country_id=country_id,
                               chapter_id=chapter_id,
                               article_id=article_id)


@router.put("/update_section/{section_id}", response_model=schemas.Section)
async def update_section(section_id: int,
                         section_update: schemas.SectionBase,
                         db: Session = Depends(get_db)):
    """Endpoint to update a section based in its id"""

    return crud.update_section(db, section_id, section_update)


@router.delete("/delete_section/{section_id}", response_model=None)
async def delete_section(section_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete a section based on its id"""

    crud.delete_section(db, section_id)
    return {"message": "Section deleted successfully"}
