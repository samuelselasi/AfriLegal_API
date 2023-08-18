from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

##

@app.post("/regions/", response_model=schemas.Region)
def create_region(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    db_region = crud.get_region_by_name(db, name=region.name)
    if db_region:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_region(db=db, region=region)


@app.get("/regions/", response_model=List[schemas.Region])
def read_regions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    regions = crud.get_regions(db, skip=skip, limit=limit)
    return regions


@app.get("/regions/{region_id}", response_model=schemas.Region)
def read_region(region_id: int, db: Session = Depends(get_db)):
    db_region = crud.get_region(db, region_id=region_id)
    if db_region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    return db_region


@app.post("/regions/{region_id}/country/", response_model=schemas.Country)
def create_country_for_region(
    region_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_region_country(db=db, country=country, region_id=region_id)


@app.get("/countries/", response_model=List[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries


@app.post("/preambles/", response_model=schemas.Preamble)
def create_preamble_for_country(
    country_id: int, preamble: schemas.PreambleCreate, db: Session = Depends(get_db)):
    return crud.create_preamble(db=db, preamble=preamble, country_id=country_id)

@app.get("/preambles/", response_model=List[schemas.Preamble])
def read_preambles_by_country(
    country_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    preambles = crud.get_preambles_by_country(db, country_id=country_id, skip=skip, limit=limit)
    return preambles

@app.get("/preambles/{preamble_id}", response_model=schemas.Preamble)
def read_preamble(preamble_id: int, db: Session = Depends(get_db)):
    db_preamble = crud.get_preamble(db, preamble_id=preamble_id)
    if db_preamble is None:
        raise HTTPException(status_code=404, detail="Preamble not found")
    return db_preamble


@app.post("/chapters/", response_model=schemas.Chapter)
def create_chapter_for_country(
    country_id: int, chapter: schemas.ChapterCreate, db: Session = Depends(get_db)):
    return crud.create_chapter(db=db, chapter=chapter, country_id=country_id)

@app.get("/chapters/", response_model=List[schemas.Chapter])
def read_chapters_by_country(
    country_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    chapters = crud.get_chapters_by_country(db, country_id=country_id, skip=skip, limit=limit)
    return chapters

@app.get("/chapters/{chapter_id}", response_model=schemas.Chapter)
def read_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = crud.get_chapter(db, chapter_id=chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return db_chapter


@app.post("/articles/", response_model=schemas.Article)
def create_article_for_country_and_chapter(
    country_id: int, chapter_id: int, article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article, country_id=country_id, chapter_id=chapter_id)

@app.get("/articles/", response_model=List[schemas.Article])
def read_articles_by_country_and_chapter(
    country_id: int, chapter_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles_by_country_and_chapter(db, country_id=country_id, chapter_id=chapter_id, skip=skip, limit=limit)
    return articles

@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@app.post("/sections/", response_model=schemas.Section)
def create_section_for_country_chapter_article(
    country_id: int, chapter_id: int, article_id: int, section: schemas.SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db=db, section=section, country_id=country_id, chapter_id=chapter_id, article_id=article_id)

@app.get("/sections/", response_model=List[schemas.Section])
def read_sections_by_country_chapter_article(
    country_id: int, chapter_id: int, article_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections_by_country_and_chapter_and_article(db, country_id=country_id, chapter_id=chapter_id, article_id=article_id, skip=skip, limit=limit)
    return sections

@app.get("/sections/{section_id}", response_model=schemas.Section)
def read_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section
