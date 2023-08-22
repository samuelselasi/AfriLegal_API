"""Module that defines orm schemas for tables"""
from typing import List, Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int
    region_id: int

    class Config:
        orm_mode = True


class RegionBase(BaseModel):
    name: str


class RegionCreate(RegionBase):
    name: str


class Region(RegionBase):
    id: int
    is_active: bool
    countries: List[Country] = []

    class Config:
        orm_mode = True


class PreambleBase(BaseModel):
    text: str


class PreambleCreate(PreambleBase):
    pass


class Preamble(PreambleBase):
    id: int
    country: Country

    class Config:
        orm_mode = True


class ChapterBase(BaseModel):
    number: int
    text: str


class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int
    country: Country

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    number: int
    title: str
    text: str


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    country: Country
    chapter: Chapter

    class Config:
        orm_mode = True


class SectionBase(BaseModel):
    number: int
    text: str


class SectionCreate(SectionBase):
    pass


class Section(SectionBase):
    id: int
    country: Country
    chapter: Chapter
    article: Article

    class Config:
        orm_mode = True


class SubsectionBase(BaseModel):
    sub: str
    text: str


class SubsectionCreate(SubsectionBase):
    pass


class Subsection(SubsectionBase):
    id: int
    country: Country
    chapter: Chapter
    article: Article
    section: Section

    class Config:
        orm_mode = True


class PDFBase(BaseModel):
    title: str

class PDFCreate(PDFBase):
    content: bytes

class PDF(PDFBase):
    id: int

    class Config:
        orm_mode = True
