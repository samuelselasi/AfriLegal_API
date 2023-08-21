"""Module that defines CRUD functions"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

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


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


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


def get_preamble(db: Session, preamble_id: int):
    return db.query(models.Preamble).filter(models.Preamble.id == preamble_id).first()

def get_preambles_by_country(db: Session, country_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Preamble).filter(models.Preamble.country_id == country_id).offset(skip).limit(limit).all()

def create_preamble(db: Session, preamble: schemas.PreambleCreate, country_id: int):
    db_preamble = models.Preamble(**preamble.dict(), country_id=country_id)
    db.add(db_preamble)
    db.commit()
    db.refresh(db_preamble)
    return db_preamble


def update_preamble(db: Session, preamble_id: int, preamble_update: schemas.PreambleBase):
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
    db_preamble = get_preamble(db, preamble_id=preamble_id)
    if db_preamble:
        db.delete(db_preamble)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Preamble not found")


def get_chapter(db: Session, chapter_id: int):
    return db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()

def get_chapters_by_country(db: Session, country_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Chapter).filter(models.Chapter.country_id == country_id).offset(skip).limit(limit).all()

def create_chapter(db: Session, chapter: schemas.ChapterCreate, country_id: int):
    db_chapter = models.Chapter(**chapter.dict(), country_id=country_id)
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


def update_chapter(db: Session, chapter_id: int, chapter_update: schemas.ChapterBase):
    db_chapter = get_chapter(db, chapter_id=chapter_id)
    if db_chapter:
        for key, value in chapter_update.dict().items():
            setattr(db_chapter, key, value)
        db.commit()
        db.refresh(db_chapter)
        return db_chapter
    else:
        raise HTTPException(status_code=404, detail="Chapter not found")


def delete_chapter(db: Session, chapter_id: int):
    db_chapter = get_chapter(db, chapter_id=chapter_id)
    if db_chapter:
        db.delete(db_chapter)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Chapter not found")


def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def get_articles_by_country_and_chapter(db: Session, country_id: int, chapter_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Article).filter(models.Article.country_id == country_id, models.Article.chapter_id == chapter_id).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate, country_id: int, chapter_id: int):
    db_article = models.Article(**article.dict(), country_id=country_id, chapter_id=chapter_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_section(db: Session, section_id: int):
    return db.query(models.Section).filter(models.Section.id == section_id).first()

def get_sections_by_country_and_chapter_and_article(db: Session, country_id: int, chapter_id: int, article_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Section).filter(models.Section.country_id == country_id, models.Section.chapter_id == chapter_id, models.Section.article_id == article_id).offset(skip).limit(limit).all()

def create_section(db: Session, section: schemas.SectionCreate, country_id: int, chapter_id: int, article_id: int):
    db_section = models.Section(**section.dict(), country_id=country_id, chapter_id=chapter_id, article_id=article_id)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def get_subsection(db: Session, subsection_id: int):
    return db.query(models.Subsection).filter(models.Subsection.id == subsection_id).first()

def get_subsections_by_country_and_chapter_and_article_and_section(db: Session, country_id: int, chapter_id: int, article_id: int, section_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Subsection).filter(models.Subsection.country_id == country_id, models.Subsection.chapter_id == chapter_id, models.Subsection.article_id == article_id, models.Subsection.section_id == section_id).offset(skip).limit(limit).all()

def create_subsection(db: Session, subsection: schemas.SubsectionCreate, country_id: int, chapter_id: int, article_id: int, section_id: int):
    db_subsection = models.Subsection(**subsection.dict(), country_id=country_id, chapter_id=chapter_id, article_id=article_id, section_id=section_id)
    db.add(db_subsection)
    db.commit()
    db.refresh(db_subsection)
    return db_subsection


def search_sections_by_keyword(db: Session, country_id: int, keyword: str, skip: int = 0, limit: int = 100):
    return db.query(models.Section).filter(models.Section.country_id == country_id, models.Section.text.ilike(f'%{keyword}%')).offset(skip).limit(limit).all()

def search_subsections_by_keyword(db: Session, country_id: int, keyword: str, skip: int = 0, limit: int = 100):
    return db.query(models.Subsection).filter(models.Subsection.country_id == country_id, models.Subsection.text.ilike(f'%{keyword}%')).offset(skip).limit(limit).all()

def search_chapters_by_keyword(db: Session, country_id: int, keyword: str, skip: int = 0, limit: int = 100):
    return db.query(models.Chapter).filter(models.Chapter.country_id == country_id, models.Chapter.text.ilike(f'%{keyword}%')).offset(skip).limit(limit).all()


def search_articles_by_keyword(db: Session, country_id: int, keyword: str, skip: int = 0, limit: int = 100):
    return db.query(models.Article).filter(models.Article.country_id == country_id, models.Article.title.ilike(f'%{keyword}%')).offset(skip).limit(limit).all()
