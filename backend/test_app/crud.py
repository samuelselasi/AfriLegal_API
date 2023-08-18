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


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def create_region_country(db: Session, country: schemas.CountryCreate, region_id: int):
    db_country = models.Country(**country.dict(), region_id=region_id)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


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
