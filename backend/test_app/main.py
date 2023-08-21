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


@app.put("/regions/{region_id}", response_model=schemas.Region)
def update_region(region_id: int, region_update: schemas.RegionBase, db: Session = Depends(get_db)):
    return crud.update_region(db, region_id, region_update)


@app.delete("/regions/{region_id}", response_model=None)
def delete_region(region_id: int, db: Session = Depends(get_db)):
    crud.delete_region(db, region_id)
    return {"message": "Region deleted successfully"}


@app.post("/regions/{region_id}/country/", response_model=schemas.Country)
def create_country_for_region(
    region_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_region_country(db=db, country=country, region_id=region_id)


@app.get("/countries/", response_model=List[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries


@app.put("/countries/{country_id}", response_model=schemas.Country)
def update_country(country_id: int, country_update: schemas.CountryBase, db: Session = Depends(get_db)):
    return crud.update_country(db, country_id, country_update)


@app.delete("/countries/{country_id}", response_model=None)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    crud.delete_country(db, country_id)
    return {"message": "Country deleted successfully"}


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


@app.put("/preambles/{preamble_id}", response_model=schemas.Preamble)
def update_preamble(
    preamble_id: int, preamble_update: schemas.PreambleBase, db: Session = Depends(get_db)
):
    return crud.update_preamble(db, preamble_id, preamble_update)


@app.delete("/preambles/{preamble_id}", response_model=None)
def delete_preamble(preamble_id: int, db: Session = Depends(get_db)):
    crud.delete_preamble(db, preamble_id)
    return {"message": "Preamble deleted successfully"}


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


@app.put("/chapters/{chapter_id}", response_model=schemas.Chapter)
def update_chapter(
    chapter_id: int, chapter_update: schemas.ChapterBase, db: Session = Depends(get_db)
):
    return crud.update_chapter(db, chapter_id, chapter_update)


@app.delete("/chapters/{chapter_id}", response_model=None)
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    crud.delete_chapter(db, chapter_id)
    return {"message": "Chapter deleted successfully"}


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


@app.put("/articles/{article_id}", response_model=schemas.Article)
def update_article(
    article_id: int, article_update: schemas.ArticleBase, db: Session = Depends(get_db)
):
    return crud.update_article(db, article_id, article_update)

@app.delete("/articles/{article_id}", response_model=None)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    crud.delete_article(db, article_id)
    return {"message": "Article deleted successfully"}


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


@app.put("/sections/{section_id}", response_model=schemas.Section)
def update_section(
    section_id: int, section_update: schemas.SectionBase, db: Session = Depends(get_db)
):
    return crud.update_section(db, section_id, section_update)

@app.delete("/sections/{section_id}", response_model=None)
def delete_section(section_id: int, db: Session = Depends(get_db)):
    crud.delete_section(db, section_id)
    return {"message": "Section deleted successfully"}


@app.post("/subsections/", response_model=schemas.Subsection)
def create_subsection_for_country_chapter_article_section(
    country_id: int, chapter_id: int, article_id: int, section_id: int, subsection: schemas.SubsectionCreate, db: Session = Depends(get_db)):
    return crud.create_subsection(
        db=db, subsection=subsection, country_id=country_id, chapter_id=chapter_id, article_id=article_id, section_id=section_id
    )

@app.get("/subsections/", response_model=List[schemas.Subsection])
def read_subsections_by_country_chapter_article_section(
    country_id: int, chapter_id: int, article_id: int, section_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subsections = crud.get_subsections_by_country_and_chapter_and_article_and_section(
        db, country_id=country_id, chapter_id=chapter_id, article_id=article_id, section_id=section_id, skip=skip, limit=limit
    )
    return subsections

@app.get("/subsections/{subsection_id}", response_model=schemas.Subsection)
def read_subsection(subsection_id: int, db: Session = Depends(get_db)):
    db_subsection = crud.get_subsection(db, subsection_id=subsection_id)
    if db_subsection is None:
        raise HTTPException(status_code=404, detail="Subsection not found")
    return db_subsection


@app.put("/subsections/{subsection_id}", response_model=schemas.Subsection)
def update_subsection(
    subsection_id: int, subsection_update: schemas.SubsectionBase, db: Session = Depends(get_db)
):
    return crud.update_subsection(db, subsection_id, subsection_update)

@app.delete("/subsections/{subsection_id}", response_model=None)
def delete_subsection(subsection_id: int, db: Session = Depends(get_db)):
    crud.delete_subsection(db, subsection_id)
    return {"message": "Subsection deleted successfully"}


# Search sections by keyword
@app.get("/search/sections/", response_model=List[schemas.Section])
def search_sections_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    sections = crud.search_sections_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return sections

# Search subsections by keyword
@app.get("/search/subsections/", response_model=List[schemas.Subsection])
def search_subsections_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    subsections = crud.search_subsections_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return subsections

# Search chapters by keyword
@app.get("/search/chapters/", response_model=List[schemas.Chapter])
def search_chapters_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    chapters = crud.search_chapters_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return chapters


# Search articles by keyword
@app.get("/search/articles/", response_model=List[schemas.Article])
def search_articles_by_keyword(
    country_id: int, keyword: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    articles = crud.search_articles_by_keyword(
        db, country_id=country_id, keyword=keyword, skip=skip, limit=limit
    )
    return articles
